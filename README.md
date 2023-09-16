# crypto_Information_bot
Это телеграмм бот, с помощью него можно получать актуальные цены монет на разных биржах, отслеживать востребованность монет в мире. Также бот определяет пользовательский рейтинг, в работе использует CoinLore Api.

This is a telegram bot, with the help of it you can get the current prices of coins on different exchanges, track the demand for coins in the world. The bot also determines the user rating, uses the CoinLore Api in its work.

# Used technology
* Python (3.10);
* aiogram(Telegram Bot framework)
* peewee(Peewee is an ORM for Python);
* SQLite(working with database from Python);

# Installation
Клонируйте репозиторий командой:

Clone the repository with the command:

```html
git clone https://github.com/krlns/crypto_Information_bot.git
```
или скачайте и добавьте проект вручную

or download and add the project manually



Установить все библиотеки из:

Install all libraries from:

`requirements.txt`

Создайте файл .env. Откройте его и заполните необходимыми данными, не забудьте указать данные для подключения к telegram(предварительно создав его в https://t.me/BotFather) и CoinLore.

Create a .env file. Open it and fill in the necessary data, do not forget to specify the data for connecting to telegram (having previously created it in https://t.me/BotFather ) and CoinLore.

Запустите файл:

Run the:

`main.py`
