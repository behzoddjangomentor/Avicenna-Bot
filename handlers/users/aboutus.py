from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from api import about
@dp.message_handler(Text(startswith="🏛 Biz haqimizda"))
async def test(message:types.Message):
    data = about()
    await message.answer(data)
