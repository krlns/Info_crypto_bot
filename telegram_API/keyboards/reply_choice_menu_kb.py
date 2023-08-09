from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from site_API.core import headers, site_api, url
import json


def get_menu_info_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню ✅")
    kb.button(text="Справка 📑")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_all_info() -> str:
    global_data = site_api.get_global_data()
    response = global_data(url, headers, {}, "global").text
    res = json.loads(response)

    return f"Мировая рыночная капитализация криптовалют на сегодня: {res[0]['total_mcap']}$ 💵\n\nОбщее количество " \
           f"криптовалют: {res[0]['coins_count']} 💳\n\nОбщее количество криптовалютных бирж: " \
           f"{res[0]['active_markets']} 💻"