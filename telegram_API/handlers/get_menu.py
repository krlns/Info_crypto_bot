from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from telegram_API.keyboards.reply_choice_menu_kb import get_all_info, get_menu_info_kb
from telegram_API.keyboards.inline_choice_menu_kb import generate_menu_kb

router = Router()  # [1]


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEJwMdkuYiC3BYcoRRpT7eM0scqKV0ItwACTwIAAladvQrPysaJZ3VllS8E')
    await message.answer(f"Привет, {message.from_user.first_name}!   👋\n"
                         "Здесь ты можешь узнать актуальную информацию о криптовалюте   🗂\n"
                         "Let's go!    🔎", reply_markup=get_menu_info_kb())


@router.message(F.text == "Меню ✅")
async def answer_menu(message: Message):
    await message.answer("Меню", reply_markup=generate_menu_kb().as_markup())


@router.message(F.text == "Справка 📑")
async def answer_info(message: Message):
    await message.answer(get_all_info())