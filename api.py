BASE_URL = 'https://avicenna.pythonanywhere.com/api/v1'
BASE_URL2 = 'https://avicenna.pythonanywhere.com/api/v2'
import requests
from datetime import datetime
import json
def create_newuser(telegram,fullname):
    url = f'{BASE_URL}/newuser/'
    reponse = requests.post(url=url,data={"telegram":telegram,"fullname":fullname})
    return 'Ok'
def getusers():
    url = f'{BASE_URL}/newuser/'
    response = requests.get(url=url)
    rest = json.loads(response.text)
    ids = []
    for i in rest:
        ids.append(i['telegram'])
    return ids
def fantest(test_kodi,tel):
    url = f'{BASE_URL}/fantest/{test_kodi}/{tel}/'
    response = requests.get(url=url)
    rest1 = json.loads(response.text)
    if rest1 == []:
        result ="❌ Bunday raqamli <b>Test</b> yoki <b>Abituriyent</b> mavjud emas!"
        return result
    else:
        rest = rest1[0]
        xato = int(rest['test_soni']) - int(rest['togri_javoblar'])
        ball = int(rest['togri_javoblar']) * 3.1
        result = f"Test sinovi | Abituriyent\n" \
                 f"FISH : <b>{rest['oquvchi']}</b>\n\n" \
                 f"_________________________\n" \
                 f"Fan nomi : <b>{rest['fan_nomi']}</b>\n" \
                 f"Savollar soni : <b>{rest['test_soni']}</b>\n" \
                 f"To'gri javoblar soni : <b>{rest['togri_javoblar']}</b>\n" \
                 f"Noto'gri javoblar soni :<b>{xato}</b>\n" \
                 f"_______________________________________\n" \
                 f"Umumiy ball : <b>{ball}</b>\n"

        return result
def checktestcode(test_kodi):
    url = f'{BASE_URL}/checkfantest/{test_kodi}/'
    response = requests.get(url=url)
    if response.status_code != 204:
        return 'Ok'
    else:
        return 'Bad'
def bloktest(week_code):
    url = f'{BASE_URL}/bloktest/{week_code}/'
    response = requests.get(url=url)
    rest= json.loads(response.text)
    if rest['week_code'] =='':
        result ="❌ Bunday raqamli <b>Abituriyent</b> mavjud emas!"
        return result
    else:
        result = f"Test sinovi | Abituriyent\n" \
                     f"FISH : <b>{rest['fio']}</b>\n\n" \
                     f"_________________________\n" \
                     f"Blok test fanlari :\n" \
                     f"1. <b>{rest['first_block']} </b>: {rest['fan1']}\n" \
                     f"2. <b>{rest['second_block']}</b>:  {rest['fan2']}\n" \
                     f"3. <b>Ona tili</b>: {rest['ona_tili']}\n" \
                     f"4. <b>Tarix</b>: {rest['tarix']}\n" \
                     f"5. <b>Matematika</b>: {rest['matematika']}\n" \
                     f"_______________________________________\n" \
                     f"Umumiy ball : <b>{rest['ball']}</b>\n"
        return result
from datetime import date


def get_block_test(global_id,chat_id):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    url = f'https://yadrosmart.uz/charts/temp.php?g_id={global_id}&tg_id={chat_id}'
    rest = requests.get(url)
    response = json.loads(rest.text)
    if response['error']:
        return response['url']
    else:
        return response['url']
def studentcount():
    url = f'{BASE_URL}/getstudentcount/'
    response = requests.get(url)
    rest = json.loads(response.text)
    return rest['count']
def botusercount():
    url = f'{BASE_URL}/getbotusercount/'
    response = requests.get(url)
    rest = json.loads(response.text)
    return rest['count']
def teachercount():
    url = f'{BASE_URL}/getteachercount/'
    response = requests.get(url)
    rest = json.loads(response.text)
    return rest['count']
def classcount():
    url = f'{BASE_URL2}/getclasscount/'
    response = requests.get(url)
    rest = json.loads(response.text)
    return rest['count']
def mydata():
    oquvchilar = studentcount()
    bot_foydalanuvchilari = botusercount()
    oqituvchi = teachercount()
    sinf = classcount()
    text =f"<b>🏫 Avitsenna maktabi statistika ma'lumotlari: </b>\n\n" \
        f"<b>👩‍🎓👨‍🎓  ‍Maktab o'quvchilari soni: </b>{oquvchilar}\n\n" \
           f"<b>👩‍🏫👨‍🏫 ‍ Maktab o'qituvchilar soni : </b> {oqituvchi}\n\n" \
           f"<b>🏠‍ Maktabdagi sinflar soni : </b> {sinf}\n\n" \
           f"<b>🤖 Bot foydalanuvchilari soni : </b> {bot_foydalanuvchilari}\n\n"
    return text

# maktab haqida ma'lumot
def about():
    oqituvchi = teachercount()
    sinf = classcount()
    text =f"<b> Qashqadaryo viloyati Qarshi shahridagi “Avitsenna school” nodavlat taʼlim muassasasi toʻgʻrisida MA’LUMOT: </b>\n\n" \
        f"<b> Direktorning FISH: Halimov Murodulla Ziyodullayevich </b>\n\n" \
           f"<b>Tayinlangan sanasi: 2020-yil 30-oktabrdan</b>\n\n" \
           f"<b>Maktabning qurilgan yili:  2020-yil </b>\n\n" \
           f"<b>Dastur asosida taʼmirlangan yili va turi:  2020-yil yangi qurilgan </b>\n\n"\
           f"<b>Sektor raqami: 1-sektor (shahar hokimi)</b>  \n\n"\
           f"<b>Maktabning yuridik  manzili :  Qarshi shahar Kunchiqar MFY</b>  \n\n"\
           f"<b> Maktab maqomi : (Nodavlat umumiy oʻrta taʼlim / ixtisoslashgan)</b> \n\n"\
           f"<b> Oʻquvchi oʻrni (quvvati):  300 oʻrinli</b> \n\n"\
           f"<b> Koeffitsiyenti : 0.7</b> \n\n"\
           f"<b> Taʼlim tili:  Oʻzbek</b> \n\n"\
           f"<b> Sinflar soni: {sinf}</b> \n\n"\
           f"<b> Oʻzbek sinflar soni  9 ta </b>\n\n"\
           f"<b> Rus sinflar soni  - </b>\n\n"\
           f"<b> Qaysi chet tili oʻqitiladi: Ingliz tili</b> \n\n"\
           f"<b> Pedagog xodimlar soni  {oqituvchi} nafar </b>\n\n"\
           f"<b> MODDIY-TEXNIK BAZASI: </b>\n\n\n"\
           f"<b> Fizika taʼmirlangan</b> \n\n"\
           f"<b> Kimyo: taʼmirlangan </b>\n\n"\
           f"<b> Sport zali holati: yangi </b> \n\n"\
           f"<b> Kutubxona holati : mavjud </b>  \n\n"\
           f"<b> Informatika fani xonasi: 10 ta mavjud barchasi yaroqli, internetga ulangan </b>\n\n"\
            f"<b> Oshxona xolati: yangi  </b>\n\n"\
            f"<b> Xojatxona xolati: yangi </b>\n\n"
    return text


def getclass():
    url = f"{BASE_URL2}/class/"
    response = requests.get(url)
    rest = json.loads(response.text)
    return rest
def getclassstudent(id):
    url = f"{BASE_URL2}/class/{id}/"
    response = requests.get(url)
    rest = json.loads(response.text)
    students = rest['student']
    count =1
    counter = 0
    my = ''
    for student in students:
        my +=f"{count}) 👤 {student['name']}\n"
        count+=1
        counter+=1
    text = f"🏫 Sinf nomi : {rest['name']}\n\n" \
           f"____________________________________\n" \
           f"🕔 Dars vaqti : {rest['lesson_time']}\n" \
           f"👨‍🏫 Sinf rahbar : {rest['tuitor']['name']}\n" \
           f"________________________________________________\n" \
           f"👨‍👨‍👧‍👧 Sinfdagi oquvchilar soni : {counter} ta \n" \
           f"Sinfdagi o'quvchilar: \n"\
           f"{my}"
    return text
def getstudentinfo(one_id):
    url = f"{BASE_URL}/studentinfo/{one_id}/"
    response = requests.get(url)
    if response.status_code==200:
        rest = json.loads(response.text)
        data  ={'status':'Ok','data':rest}
        return data
    else:
        data = {'status': 'Bad'}
        return data
def get_result_image(test_kodi,tel):
    url = f"https://yadrosmart.uz/charts/images/temp.php?test_code={test_kodi}&pn={tel}"
    requests.get(url)
    return 'Ok'

