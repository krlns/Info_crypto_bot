import json
from aiogram import Bot, Dispatcher
from settings_data.settings import BotSettings
from site_API.core import headers, querystring_tickers, site_api, url
from database.common.models import database, History
from database.core import crud
from telegram_API.handlers import get_menu
from telegram_API.handlers import get_coin_prices
from telegram_API.handlers import top_expensive_inexpensive
from telegram_API.handlers import get_rating_coin


bot_settings = BotSettings()
bot = Bot(token=bot_settings.bot_token.get_secret_value())
dp = Dispatcher()


async def fill_db() -> None:
    querystring_tickers['limit'] = "100"
    response = site_api.get_data_tickers()
    response = response(url, headers, querystring_tickers, "tickers").text
    data = json.loads(response)

    write = crud.create()
    data_source = [{"name_coin": data['data'][el]['symbol'], "numbers_of_cliks": 0} for el in range(len(data['data']))]
    write(database, History, data_source)

    querystring_tickers['limit'] = "15"


async def main() -> None:
    dp.include_routers(get_menu.router)
    dp.include_routers(get_coin_prices.router_get_coin_prices)
    dp.include_routers(top_expensive_inexpensive.router_for_coin_prices)
    dp.include_routers(get_rating_coin.router_get_rating_coin)

    await bot.delete_webhook(drop_pending_updates=True)
    await fill_db()

    await dp.start_polling(bot)
