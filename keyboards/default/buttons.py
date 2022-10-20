from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
main = ReplyKeyboardMarkup(resize_keyboard=True,
                           keyboard=[
                               [
                                   KeyboardButton(text="🎓 O'quvchi haqida"),
                                  
                                   KeyboardButton(text="📊 Statistika"),
                                   
                               ],
[

                                   KeyboardButton(text="✅ Natijalar"),
                                   KeyboardButton(text="🏛 Biz haqimizda")
                               ]
                           ])
number = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [KeyboardButton(text='📞 Telefon raqamni ulashish',request_contact=True)]
                             ])
testlar = ReplyKeyboardMarkup(resize_keyboard=True,
                              keyboard=[
                                  [KeyboardButton(text="🧪 Fan testlari"),
                                   KeyboardButton(text="📑 Blok testlar")],
                                  [

                                      KeyboardButton(text="◀ Orqaga")
                                  ]
                              ])
backbutton = ReplyKeyboardMarkup(resize_keyboard = True,
                                 keyboard = [
                                   [  KeyboardButton(text= "🔙 Orqaga")]
                                 ])