from aiogram.utils.keyboard import InlineKeyboardBuilder


def generate_menu_kb() -> InlineKeyboardBuilder:
    menu = InlineKeyboardBuilder()
    menu.button(text="Cтоимость монет 💰", callback_data="coin_info_prices")
    menu.button(text="Топ дорогостоящих ⬆️", callback_data="top_expensive")
    menu.button(text="Топ малобюджетных ⬇️", callback_data="top_inexpensive")
    menu.button(text="Рейтинг 🔥", callback_data="history_requests")
    menu.adjust(2)
    return menu

