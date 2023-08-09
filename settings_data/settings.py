import os

from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

if not find_dotenv():
    exit("Переменные окружения не загружены, отсутствует файл .env")
else:
    load_dotenv()


class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv('SITE_API', None)
    host_api: StrictStr = os.getenv('HOST_API', None)


class BotSettings(BaseSettings):
    bot_token: SecretStr = os.getenv('BOT_TOKEN', None)
