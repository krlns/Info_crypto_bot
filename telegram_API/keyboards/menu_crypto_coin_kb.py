import json
from typing import Dict
from aiogram.utils.keyboard import InlineKeyboardBuilder
from site_API.core import headers, querystring_tickers, querystring_markets, site_api, url


def generate_coin_kb() -> InlineKeyboardBuilder:
    response = get_coin_info()

    left = int(querystring_tickers['start']) - 15 if int(querystring_tickers['start']) != 0 else \
        querystring_tickers['start']
    right = int(querystring_tickers['start']) + 15

    coins = InlineKeyboardBuilder()
    for i in range(len(response)):
        coins.button(text=f"{response[i]['symbol']}", callback_data=f"id_{response[i]['id']}")
    coins.button(text="Назад ⬅️", callback_data=f"page:{left}")
    coins.button(text="➡️ Вперед", callback_data=f"page:{right}")
    coins.adjust(3)
    return coins


def get_coin_info() -> Dict:
    coin_info = site_api.get_data_tickers()
    response = coin_info(url, headers, querystring_tickers, "tickers").text
    data = json.loads(response)
    return data["data"]


def generate_markets_kb() ->  InlineKeyboardBuilder:
    response = get_markets_info()
    markets_name_list = []

    markets = InlineKeyboardBuilder()
    for i in range(15):
        if response[i]['name'] not in markets_name_list:
            markets_name_list.append(response[i]['name'])  # Removes duplicate names of cryptocurrency exchanges
            markets.button(text=f"{response[i]['name']}", callback_data=f"market_{response[i]['name']}")
    markets.adjust(3)
    return markets


def get_markets_info() -> Dict:
    markets_info = site_api.get_data_markets()
    response = markets_info(url, headers, querystring_markets, "coin", "markets").text
    data = json.loads(response)
    return data
