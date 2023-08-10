from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import json
from typing import Dict
from site_API.core import headers, querystring_tickers, site_api, url


router_for_coin_prices = Router()  # [3]


def get_info_price() -> Dict:
    prices = {}
    querystring_tickers['limit'] = "100"
    start = querystring_tickers['start']
    querystring_tickers['start'] = "0"

    coin_prices = site_api.get_data_tickers()
    response = coin_prices(url, headers, querystring_tickers, "tickers").text

    querystring_tickers['limit'] = "15"
    querystring_tickers['start'] = start

    data = json.loads(response)
    for info in data['data']:
        prices[info['symbol']] = info['price_usd']
    return prices


def sorted_price(flag: bool) -> str:
    sorted_coin = sorted(get_info_price().items(), key=lambda item: float(item[1]), reverse=flag)

    return f"Топ {'дорогостоящих' if flag else 'малобюджетных'} криптовалют за последние 24 часа 🕐\n\n" \
           f"1️⃣ {sorted_coin[0][0]} стоимостью {sorted_coin[0][1]}$ 💵\n" \
           f"2️⃣ {sorted_coin[1][0]} стоимостью {sorted_coin[1][1]}$ 💵\n" \
           f"3️⃣ {sorted_coin[2][0]} стоимостью {sorted_coin[2][1]}$ 💵\n" \
           f"4️⃣ {sorted_coin[3][0]} стоимостью {sorted_coin[3][1]}$ 💵\n" \
           f"5️⃣ {sorted_coin[4][0]} стоимостью {sorted_coin[4][1]}$ 💵"


@router_for_coin_prices.callback_query(F.data == "top_expensive")
async def info_of_top_expensive(callback: CallbackQuery):
    await callback.message.answer(sorted_price(True))


@router_for_coin_prices.callback_query(F.data == "top_inexpensive")
async def info_of_top_inexpensive(callback: CallbackQuery):
    await callback.message.answer(sorted_price(False))