from aiogram.dispatcher.filters import Text
from aiogram import types
BASE_URL = 'https://avicenna.pythonanywhere.com'
from loader import dp
from api import getstudentinfo
from aiogram.dispatcher.filters.builtin import CallbackQuery
from aiogram.dispatcher import FSMContext
from states.ResultState import StudentInfo
@dp.message_handler(Text(startswith="🎓 O'quvchi haqida"),state=None)
async def start(message:types.Message):
    await message.answer("Ma'lumot olish uchun One_ID ingizni yuboring!")
    await StudentInfo.one_id.set()
@dp.message_handler(state=StudentInfo.one_id)
async def getinfo(message:types.Message,state:FSMContext):
    one_id = message.text
    datas = getstudentinfo(one_id)
    if datas['status'] =='Ok':
        datas = datas['data']

        if datas == []:
            await message.answer("Malumot topilmadi!")
            await state.finish()
        else:
            for data in datas:
                talaba = data['name']
                phone = data['phone']
                caption = ''
                payment = ''
                count = 1
                sum =0
                for i in data['paymentstudent']:
                    a = i['date']
                    import dateutil.parser
                    a = dateutil.parser.parse(a)
                    sana = a.strftime("%m/%d/%Y, %H:%M:%S")
                    description = i['description']
                    sum += int(i['sum'])
                    payment += f"{count}) 💴 To'lov qilingan summa: <b>{i['sum']}</b> so'm\n" \
                               f"     📆 To'lov qilingan vaqt : <b>{sana}</b>\n" \
                               f"     ✏ To'lov uchun izoh: <b>{description}</b>\n"
                    count+=1
                caption += f"👨‍🎓 O'quvchi ismi: <b>{talaba}</b>\n" \
                           f"📲 Telefon raqami : <b>{phone}</b>\n" \
                           f"___________<b>To'lov haqida ma'lumot</b>__________\n" \
                           f"{payment}\n" \
                           f"💲 Umumiy to'lov: <b>{sum}</b> so'm"
                await message.answer_photo(photo=BASE_URL+data['image'],caption=caption)
                await state.finish()
    else:
        await message.answer("Malumot topilmadi!")
        await state.finish()



