from aiogram import types
from loader import  dp,bot
from api import  getusers
@dp.channel_post_handler(content_types=types.ContentType.ANY)
async def send(message:types.Message):
    allusers = getusers()
    message_id = message.message_id
    for i in allusers:
        await bot.forward_message(chat_id=i,from_chat_id=-1001851774717,message_id=message_id)