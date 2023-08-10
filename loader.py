from aiogram import Bot, Dispatcher
from settings_data.settings import BotSettings
from telegram_API.handlers import get_menu
from telegram_API.handlers import get_coin_prices
from telegram_API.handlers import top_expensive_inexpensive
from telegram_API.handlers import get_rating_coin
from database.core import fill_db
from aiogram.fsm.strategy import FSMStrategy
from aiogram.fsm.storage.memory import MemoryStorage

bot_settings = BotSettings()
bot = Bot(token=bot_settings.bot_token.get_secret_value())
dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)


async def main() -> None:
    dp.include_routers(get_menu.router)
    dp.include_routers(get_coin_prices.router_get_coin_prices)
    dp.include_routers(top_expensive_inexpensive.router_for_coin_prices)
    dp.include_routers(get_rating_coin.router_get_rating_coin)

    await bot.delete_webhook(drop_pending_updates=True)
    await fill_db()

    await dp.start_polling(bot)
