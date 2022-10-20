from aiogram.dispatcher.filters.builtin import Command,CallbackQuery
from aiogram import types
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from states.ResultState import CheckResult,BlokTestState
from api import fantest,checktestcode,bloktest,get_block_test, about,get_result_image
from keyboards.default.buttons import number,main,testlar,backbutton
from aiogram.dispatcher.filters import  Text
@dp.message_handler(Text(startswith="📑 Blok testlar"),state=None)
async def one(message:types.Message):
    await message.answer("Shaxsiy Global id ni yuboring!")
    await BlokTestState.global_id.set()
@dp.message_handler(state=BlokTestState.global_id)
async def two(message:types.Message,state:FSMContext):
    global_id = message.text
    chat_id = message.from_user.id
    result = get_block_test(global_id=global_id,chat_id=chat_id)
    if result=='Bad':
        await message.answer("Ushbu Global Id orqali ma'lumot topilmadi!",reply_markup=main)
        await state.finish()
    else:
        await message.answer_photo(photo=result,reply_markup=main)
        await state.finish()


@dp.message_handler(Text(startswith="◀ Ortga"))
async def start(message:types.Message):
    await message.answer(f"Kerakli bo'limni tanlang!",reply_markup=main)
@dp.message_handler(Text(startswith='✅ Natijalar'),state=None)
async def zero(message:types.Message):
    await message.answer("Kerakli bo'limni tanlang!",reply_markup=testlar)

@dp.message_handler(Text(startswith='🧪 Fan testlari'),state=None)
async def one(message:types.Message):
    await message.answer("Iltimos test kodini kiriting!\n"
                         "Masalan: <b>12a258</b>!")
    await CheckResult.test_code.set()
@dp.message_handler(state=CheckResult.test_code)
async def two(message:types.Message,state:FSMContext):
    test_kodi = message.text
    if test_kodi == "🔙 Orqaga":
        await message.answer("Kerakli bo'limni tanlang!", reply_markup=testlar)
        await state.finish()
    else:
        check = checktestcode(test_kodi=test_kodi)
        if check == 'Ok':
            await state.update_data({
                'test_kodi': test_kodi
            })
            await message.answer(f"Telefon raqamingizni ulashing:\n"
                                 f"1.<b>+998996671529</b> ko'rinishida yoki\n"
                                 f"2.<b>Telefon raqamni ulashish</b> tugmasini bosing!", reply_markup=number)
            await CheckResult.next()
        else:
            await message.answer("<b>❌ Bunaqa kodli test mavjud emas!</b>\n\n"
                                 "🔄 <b>Iltimos test kodini qayta kiriting!</b>", reply_markup=backbutton)
            await CheckResult.test_code.set()


@dp.message_handler(state=CheckResult.phone,content_types=types.ContentType.ANY)
async def three(message:types.Message,state:FSMContext):

    if message.content_type =='contact':
       tel = message.contact.phone_number
       await state.update_data({
           'tel': tel
       })
       data = await state.get_data()
       tel = data['tel']
       result = fantest(test_kodi=data['test_kodi'], tel=data['tel'])
    #    natija =get_result_image(test_kodi=data['test_kodi'], tel=tel[1:])
    #    if not natija['errorser']:
    #         if not natija['error']:
    #           await message.answer_photo(photo=natija['url'],caption=result) 
    #           await message.answer_document(document=natija['urlser'])
    #    elif not natija['error']:
    #         await message.answer_photo(photo=natija['url'],caption=result)
    #    else:
    #         await message.answer("<b>Ma'lumot topilmadi!</b>")
       await message.answer(result)
       await state.finish()
    else:
        tel = message.text
        if tel.startswith('+998'):
            await state.update_data({
                'tel': tel
            })
            data = await state.get_data()
            tel = data['tel']
            result = fantest(test_kodi=data['test_kodi'], tel=data['tel'])
            # natija = get_result_image(test_kodi=data['test_kodi'], tel=tel[1:])
            # if not natija['errorser']:
            #     if not natija['error']:
            #         await message.answer_photo(photo=natija['url'], caption=result)
            #         await message.answer_document(document=natija['urlser'])
            # elif not natija['error']:
            #     await message.answer_photo(photo=natija['url'], caption=result)
            # else:
            #     await message.answer("<b>Ma'lumot topilmadi!</b>")
            await message.answer(result)
            await state.finish()
        else:
            await message.answer(f"Telefon raqamingizni ulashing:\n"
                                 f"1.<b>+998996671529</b> ko'rinishida yoki\n"
                                 f"2.<b>Telefon raqamni ulashish</b> tugmasini bosing!")
            await CheckResult.phone.set()




