from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
main = ReplyKeyboardMarkup(resize_keyboard=True,
                           keyboard=[
                               [
                                   KeyboardButton(text="๐ O'quvchi haqida"),
                                  
                                   KeyboardButton(text="๐ Statistika"),
                                   
                               ],
[

                                   KeyboardButton(text="โ Natijalar"),
                                   KeyboardButton(text="๐ Biz haqimizda")
                               ]
                           ])
number = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [KeyboardButton(text='๐ Telefon raqamni ulashish',request_contact=True)]
                             ])
testlar = ReplyKeyboardMarkup(resize_keyboard=True,
                              keyboard=[
                                  [KeyboardButton(text="๐งช Fan testlari"),
                                   KeyboardButton(text="๐ Blok testlar")],
                                  [

                                      KeyboardButton(text="โ Orqaga")
                                  ]
                              ])
backbutton = ReplyKeyboardMarkup(resize_keyboard = True,
                                 keyboard = [
                                   [  KeyboardButton(text= "๐ Orqaga")]
                                 ])