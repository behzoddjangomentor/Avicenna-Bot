from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
from api import getclass,getclassstudent
@dp.message_handler(Text(startswith='๐ Sinflar'))
async def test(message:types.Message):
    data = getclass()
    button = InlineKeyboardMarkup(row_width=3)
    for i in data:
        a = InlineKeyboardButton(text=i['name'],callback_data=f"โ{i['id']}")
        button.insert(a)

    await message.answer("Kerakli sinfni tanlang!",reply_markup=button)
@dp.callback_query_handler(Text(startswith='โ'))
async def studentdata(call:CallbackQuery):
    await call.answer(cache_time=60)
    id =call.data
    id = id[1:]
    data = getclassstudent(id)
    button = InlineKeyboardMarkup()
    button.add(InlineKeyboardButton(text='๐ Orqaga',callback_data='๐orqaga'))
    await call.message.delete()
    await call.message.answer(data,reply_markup=button)
@dp.callback_query_handler(text='๐orqaga')
async def first(call:CallbackQuery):
    await call.answer(cache_time=60)
    data = getclass()
    button = InlineKeyboardMarkup(row_width=3)
    for i in data:
        a = InlineKeyboardButton(text=i['name'], callback_data=f"โ{i['id']}")
        button.insert(a)
    await call.message.delete()
    await call.message.answer("Kerakli sinfni tanlang!", reply_markup=button)