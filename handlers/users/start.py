from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import main
from loader import dp
from aiogram.dispatcher.filters import Text
from api import mydata

from api import create_newuser
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram = message.from_user.id
    fullname = message.from_user.full_name
    create_newuser(telegram,fullname)
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}</b>!\n"
                         f"<i>Avitsenna Maktabi Rasmiy Botiga Xush Kelibsiz!</i>\n"
                         f"Kerakli bo'limni tanlang!",reply_markup=main)
@dp.message_handler(Text(startswith = "📊 Statistika"))
async def test(message:types.Message):
    data = mydata()
    await message.answer(data)