from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from telegram_API.keyboards.menu_crypto_coin_kb import generate_coin_kb, generate_markets_kb, get_markets_info, get_coin_info
from site_API.core import querystring_tickers, querystring_markets
from database.common.models import History


router_get_coin_prices = Router()  # [2]


async def update_coins(message: Message):
    await message.edit_reply_markup("Выбери монету", reply_markup=generate_coin_kb().as_markup())


@router_get_coin_prices.callback_query(F.data == "coin_info_prices")
async def get_pricing_information(callback: CallbackQuery):
    await callback.message.answer("Выбери монету", reply_markup=generate_coin_kb().as_markup())


@router_get_coin_prices.callback_query(F.data == "list_next")
async def scroll_forward(callback: CallbackQuery):
    edit_num = int(querystring_tickers['start']) + 15
    querystring_tickers['start'] = str(edit_num)
    await update_coins(callback.message)


@router_get_coin_prices.callback_query(F.data == "list_back")
async def scroll_back(callback: CallbackQuery):
    if int(querystring_tickers['start']) != 0:
        edit_num = int(querystring_tickers['start']) - 15
        querystring_tickers['start'] = str(edit_num)
        await update_coins(callback.message)


@router_get_coin_prices.callback_query(F.data.startswith("id_"))
async def get_markets(callback: CallbackQuery):
    querystring_markets['id'] = callback.data.split('_')[1]
    await callback.message.answer("Выберите маркетплейс", reply_markup=generate_markets_kb().as_markup())


def get_percent_change() -> str:
    querystring_tickers['limit'] = '100'
    response_tickers = get_coin_info()
    querystring_tickers['limit'] = '15'

    for index, dict_ in enumerate(response_tickers):
        if dict_.get('id') == querystring_markets['id']:
            return f"Процент изменения: (1ч: {'📉' if dict_['percent_change_24h'] <= dict_['percent_change_1h'] else '📈'} " \
                   f"{dict_['percent_change_1h']}%)"


@router_get_coin_prices.callback_query(F.data.startswith("market_"))
async def get_info_prices_of_coin(callback: CallbackQuery):
    response_markets = get_markets_info()

    for name in response_markets:
        if name['name'] == callback.data.split('_')[1]:
            await callback.message.answer(
                f"Площадка: {name['name']} 🛍\n"
                f"Наименование монеты: {name['base']} 💳\n"
                f"Стоимть: {name['price']}$ 💰\n"
                f"{get_percent_change()}"
            )
            await callback.message.delete()

            query = History.update(numbers_of_cliks=History.numbers_of_cliks + 1).where(History.name_coin == name['base'])
            query.execute()
            break
