from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from telegram_API.keyboards.menu_crypto_coin_kb import generate_coin_kb, generate_markets_kb, get_markets_info
from site_API.core import querystring_tickers, querystring_markets
from database.common.models import database, History
from database.core import crud

router_get_rating_coin = Router()  # [4]


def generate_rating() -> str:
    read = crud.retrieve()
    retrieved = read(database, History, History.name_coin, History.numbers_of_cliks)
    retrieved = [[el.name_coin, el.numbers_of_cliks] for el in retrieved]
    sorted_data = sorted(retrieved, key=lambda item: float(item[1]), reverse=True)
    return f"Три самые просматриваемые монеты 📊\n\n" \
           f"{sorted_data[0][0]}: {sorted_data[0][1]} 👁‍🗨\n" \
           f"{sorted_data[1][0]}: {sorted_data[1][1]} 👁‍🗨\n" \
           f"{sorted_data[2][0]}: {sorted_data[2][1]} 👁‍🗨\n"


@router_get_rating_coin.callback_query(F.data == "history_requests")
async def get_pricing_information(callback: CallbackQuery):
    await callback.message.answer(generate_rating())
