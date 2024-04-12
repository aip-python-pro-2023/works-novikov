import os
from dotenv import load_dotenv
import telebot
from telebot import types
import random


load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)
pic_muravei = "https://cdn-edge.kwork.ru/files/portfolio/t3/78/314e91808525b26c7e57a5392816239a6b2197be-1691038968.gif"
pic_bogomol = "https://img.pikbest.com/png-images/qianku/pixel-drawing-insect-mantis_2272581.png!sw800"
pic_pole = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIWI1JEY07dmBler0RKSelI90B77HSxzXhpmenK8R6LHaSNv7afa7XDnxK1UpvJNDKOw0&usqp=CAU"
pic_muravyi = "https://avatars.yandex.net/get-games/1890793/2a000001876b286899c95865b62687ab33d1/pjpg160x160"
pic_les = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX1YgDDzzat1aVE6hYtJCCQugHEB8z-PX2ww&usqp=CAU"
pic_listok= "https://img.freepik.com/premium-vector/leaf-logo-icon-in-pixel-art_588783-270.jpg"
pic_pauk="https://static.vecteezy.com/system/resources/previews/023/685/239/original/pixel-art-illustration-spider-pixelated-spider-insect-creepy-enemy-spider-pixelated-for-the-pixel-art-game-and-icon-for-website-and-video-game-old-school-retro-vector.jpg"

## начало обучения
################################################################################################

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("создать колонию 🏡")
    bot.send_photo(message.chat.id, pic_pole)
    bot.send_message(message.chat.id, 'привет , сейчас ты на поле , нажми на кнопку чтобы создать колонию',
                     reply_markup=markup)
    bot.register_next_step_handler(message, act1, "создать колонию 🏡")



## создание колонии

def act1(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("2", "3", "4")

    if message.text == "создать колонию 🏡":
        bot.send_message(message.chat.id, 'хорошо ,но что бы все получилось ты должен ответить на вопрос',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'сколько пар лап у муравьев', reply_markup=markup)
        bot.register_next_step_handler(message, act2, "")
    else:
        bot.register_next_step_handler(message, act1, "")

## путешествие

def act2(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == "3":
        bot.send_photo(message.chat.id, pic_muravyi)
        bot.send_message(message.chat.id, 'отлично , теперь у тебя есть собственная колония муравьев ',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'для существования твоей колонии нужны ресурсы',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'нажми на кнопку "путешествия" и выбери лес что бы найти еду',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act3, "")
    else:
        bot.register_next_step_handler(message, act2, "")

## вход в лес

def act3(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("лес 🌲")


    if message.text == "путешествия 🎒":
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act4, "")
    else:
        bot.register_next_step_handler(message, act3, "")
## поиск еды

def act4(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("искать еду 🥪")

    if message.text == "лес 🌲":
        os.environ["price_s_f"] = "30"

        bot.send_photo(message.chat.id, pic_les)
        bot.send_message(message.chat.id, 'хорошо , ты зашел в лес , выбери в возможных действиях "искать еду"',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'чтобы найти еду нужно ответить на вопрос', reply_markup=markup)
        bot.register_next_step_handler(message, act5, "")
    else:
        bot.register_next_step_handler(message, act4, "")
## вопрос

def act5(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("2", "3", "4")

    if message.text == "искать еду 🥪":
      bot.send_message(message.chat.id, 'сколько желудков у одного муравья?', reply_markup=markup)
      bot.register_next_step_handler(message, act6, "")
    else:
        bot.register_next_step_handler(message, act5, "")

## ахождение листка

def act6(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("собрать")

    if message.text == "2":
        bot.send_photo(message.chat.id, pic_listok)
        bot.send_message(message.chat.id, 'уровень 1 опыт 5/200', reply_markup=markup)
        bot.send_message(message.chat.id, 'помни что каждые 200 едениц опыта уровень повышается', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты обноружил листок 🌿 (15) , прикажи своим муравьям забрать его',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act7, "")
    else:
        bot.register_next_step_handler(message, act6, "")

## ускорение сбора

def act7(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == "собрать":
     bot.send_message(message.chat.id, 'сбор окончен', reply_markup=markup)
     bot.send_message(message.chat.id, 'склад : + 15 🌿', reply_markup=markup)
     os.environ["sklad"] = "15"
     os.environ["sklad_max"] = "30"
     os.environ["laky_f"] = "0"
     os.environ["price_l_f"] = "30"
     bot.send_message(message.chat.id, 'хорошо , а теперь вернись в колонию', reply_markup=markup)
     bot.register_next_step_handler(message, act8, "")
    else:
        bot.register_next_step_handler(message, act7, "")

## путешествие

def act8(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("колония 🏡")


    if message.text == "путешествия 🎒":
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act9, "")
    else:
        bot.register_next_step_handler(message, act8, "")

## нападение

def act9(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("4","8","6")


    if message.text == "колония 🏡":
        bot.send_photo(message.chat.id, pic_pauk)
        bot.send_message(message.chat.id, 'похоже что на тебя напал паук 🕷️ (20❤️), чтобы его атаковать тебе нужно получить ход, для этого ответь на вопрос', reply_markup=markup)
        bot.send_message(message.chat.id, 'сколько будет 2 + 2 * 2 = ?', reply_markup=markup)
        bot.register_next_step_handler(message, act10, "")
    else:
        bot.register_next_step_handler(message, act9, "")

def act10(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("атаковать ⚔")


    if message.text == "6":
        bot.send_message(message.chat.id, 'ты получаешь возможность атаки', reply_markup=markup)
        bot.register_next_step_handler(message, act11, "")
    else:
        bot.register_next_step_handler(message, act10, "")
## атака

def act11(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("1","0","2")


    if message.text == "атаковать ⚔":
        bot.send_message(message.chat.id, 'паук 🕷️ (10❤️/20❤️)', reply_markup=markup)
        bot.send_message(message.chat.id, 'состояние здоровья (10❤️/10❤️) , состояние хитина (20🛡️/20🛡️)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты нанес пауку удар , сейчас он может тебя атакать, ты можешь защититься правильно ответив на вопрос !', reply_markup=markup)
        bot.send_message(message.chat.id, 'сколько будет 1 * 1 - 1 = ?', reply_markup=markup)
        bot.register_next_step_handler(message, act12, "")
    else:
        bot.register_next_step_handler(message, act11, "")

def act12(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("защититься 🛡️")


    if message.text == "0":
        bot.send_message(message.chat.id, 'защищайся!', reply_markup=markup)
        bot.register_next_step_handler(message, act13, "")
    else:
        bot.register_next_step_handler(message, act12, "")
## защита

def act13(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("81","93","91")


    if message.text == "защититься 🛡️":
        bot.send_message(message.chat.id, 'состояние здоровья (10❤️/10❤️) , состояние хитина (5🛡️/20🛡️)', reply_markup=markup)
        bot.send_message(message.chat.id, "ты выдержал удар , но паук повредил твою хитиновую оболочку чтобы пополнять запас здоровья нужно вернуться в колонию" , reply_markup=markup)
        bot.send_message(message.chat.id, 'продолжай атаку', reply_markup=markup)
        bot.send_message(message.chat.id, '10 * 10 - 2 * 4 - 1 = ?', reply_markup=markup)
        bot.register_next_step_handler(message, act14, "")
    else:
        bot.register_next_step_handler(message, act13, "")


def act14(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("атаковать ⚔")

    if message.text == "91":
        bot.send_message(message.chat.id, 'остался последний удар', reply_markup=markup)
        bot.register_next_step_handler(message, act15, "")
    else:
        bot.register_next_step_handler(message, act14, "")

## победа

def act15(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == "атаковать ⚔":
        bot.send_message(message.chat.id, 'паук 🕷️ (0 ❤️)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты одержал победу над врагом , теперь ты можешь спокойно вернуться в колонию', reply_markup=markup)
        bot.send_message(message.chat.id, 'уровень 1 опыт 20/200', reply_markup=markup)
        os.environ["exp"] = "20"
        os.environ["level"] = "1"
        bot.register_next_step_handler(message, act16, "")
    else:
         bot.register_next_step_handler(message, act15, "")
## путешествие


def act16(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("колония 🏡")


    if message.text == "путешествия 🎒":
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act17, "")
    else:
        bot.register_next_step_handler(message, act16, "")

## вход в колонию

def act17(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("🎉 начать свободную игру 🎉")

    if message.text == "колония 🏡":
        bot.send_photo(message.chat.id, pic_muravyi)
        os.environ["location"] = "kolonya"
        os.environ["r"] = "2"
        os.environ["hp"] = "10"
        os.environ["hp_max"] = "10"
        os.environ["hetin"] = "5"
        os.environ["hetin_max"] = "20"
        os.environ["damage"] = "10"
        bot.send_message(message.chat.id, 'ты вернулся в колонию', reply_markup=markup)
        bot.send_message(message.chat.id, 'здесь ты можешь улучшать её и воссотанавливать здоровье  , '
                                          'а сейчас твоё обучение закончино , удачи!', reply_markup=markup)
        bot.register_next_step_handler(message, act18, "")
    else:
        bot.register_next_step_handler(message, act17, "")


def act18(message, right_answer: str):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)


    if  ((os.environ["location"] == "les") or (message.text == "лес 🌲")) and (os.environ["r"] == "1"):
        markup.add("искать еду 🥪", "искать врага ⚔","путешествия 🎒")
        os.environ["location"] = "les"
        if message.text == "лес 🌲":
          bot.send_photo(message.chat.id, pic_les)
          bot.send_message(message.chat.id, 'Ты зашел в лес', reply_markup=markup)
        bot.send_message(message.chat.id, 'выбери действие', reply_markup=markup)

        bot.register_next_step_handler(message, act19, "")

    elif  ((os.environ["location"] == "kolonya") or (message.text == "колония 🏡"))and(os.environ["r"] == "2"):
        markup.add("путешествия 🎒","улучшить колонию ⭐","cтатистика колонии ℹ️",)
        if int(os.environ["hp"]) < int(os.environ["hp_max"]) or int(os.environ["hetin"]) < int(os.environ["hetin_max"]):
            os.environ["price_hp"] = str((int(os.environ["hp_max"]) - int(os.environ["hp"]) + int(os.environ["hetin_max"]) - int(os.environ["hetin"]))*2)
            btn1 = "пополнить здоровье ❤️(" + os.environ["price_hp"] + '🌿)'
            markup.add(btn1)
        os.environ["location"] = "kolonya"
        if message.text == "колония 🏡":
          bot.send_photo(message.chat.id, pic_muravyi)
          bot.send_message(message.chat.id, 'Ты вернулся в колонию', reply_markup=markup)
        bot.send_message(message.chat.id, 'выбери действие', reply_markup=markup)

        bot.register_next_step_handler(message, act19, "")
    else:
        bot.register_next_step_handler(message, act18, "")
##лес

def act19(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    if message.text == "путешествия 🎒" :
        if os.environ["location"] != "les":
            markup.add("лес 🌲")
            os.environ["r"] = "1"
        if os.environ["location"] != "kolonya":
            markup.add("колония 🏡")
            os.environ["r"] = "2"
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act18, "")

    elif message.text == "искать еду 🥪" :
        markup.add("ответить")
        os.environ["target"] = "eda"
        bot.send_message(message.chat.id, 'чтобы найти еду нужно решить задачу', reply_markup=markup)
        bot.register_next_step_handler(message, act20, "")

    elif message.text == "улучшить колонию ⭐":
        markup.add("1⭐","2⭐","3⭐")
        bot.send_message(message.chat.id, 'список возможных улучшений:', reply_markup=markup)
        sklad_f = '1) + макс. скалад на 15🌿 (' + os.environ["price_s_f"] + "🌿)"
        bot.send_message(message.chat.id, sklad_f, reply_markup=markup)

        laky_f = "2) + 2🌿 к каждому найденному листу(" + os.environ["price_l_f"] + "🌿)"
        bot.send_message(message.chat.id, laky_f, reply_markup=markup)

        os.environ["price_hp"] = str(int(os.environ["hp_max"]) + 5)
        hp = "3)  макс.хп + 1❤️(" + os.environ["price_hp"] + "🌿)"
        bot.send_message(message.chat.id, hp, reply_markup=markup)

        bot.register_next_step_handler(message, act23, "")
    elif message.text == "cтатистика колонии ℹ️":
        level = 'ваш уровень : ' + os.environ["level"]
        markup.add("продолжить")
        bot.send_message(message.chat.id, level, reply_markup=markup)
        exp ='опыт : '+ os.environ["exp"] + "/200"
        bot.send_message(message.chat.id, exp, reply_markup=markup)
        sklad = os.environ["sklad"] + "🌿/" + os.environ["sklad_max"] + "🌿"
        bot.send_message(message.chat.id, sklad, reply_markup=markup)
        hp = "здоровье : " + os.environ["hp"] + "❤️/" + os.environ["hp_max"] + "    " + os.environ["hetin"] + "🛡️/" +  os.environ["hetin_max"] + "🛡️"
        bot.send_message(message.chat.id, hp, reply_markup=markup)
        bot.register_next_step_handler(message, act18, "")
    elif  message.text == "пополнить здоровье ❤️(" + os.environ["price_hp"] + '🌿)':
        markup.add("продолжить")
        if int(os.environ["sklad"]) >= int(os.environ["price_hp"]):
            os.environ["sklad"] = str(int(os.environ["sklad"]) - int(os.environ["price_hp"]))
            os.environ["hp"] = os.environ["hp_max"]
            os.environ["hetin"] = os.environ["hetin_max"]
            bot.send_message(message.chat.id, "🎉 исцеление успешно 🎉", reply_markup=markup)
            sklad = "склад : " + os.environ["sklad"] + "🌿/" + os.environ["sklad_max"] + "🌿"
            bot.send_message(message.chat.id, sklad, reply_markup=markup)
            hp = "здоровье : (" + os.environ["hp"] + "❤️/" + os.environ["hp_max"] + ")    (" + os.environ["hetin"] + "🛡️/" + os.environ["hetin_max"] + "🛡️)"
            bot.send_message(message.chat.id, hp, reply_markup=markup)
            bot.register_next_step_handler(message, act18, "")
        else:
            bot.send_message(message.chat.id, "❗ не хватает средств ❗", reply_markup=markup)
            bot.register_next_step_handler(message, act18, "")

    elif message.text == "искать врага ⚔":
        number = random.randint(1, 2)
        if number == 1:
            markup.add("сражение ⚔")
            os.environ["en"] = "pauk"
            os.environ["damage_en"] = str(random.randint(10, 17))
            bot.send_photo(message.chat.id, pic_pauk)
            os.environ["en_hp"] = str(random.randint(15, 25))
            p = "ты встретил паука 🕷️(" + os.environ["en_hp"] + "❤️)(" + os.environ["damage_en"] + "⚔)"
            bot.send_message(message.chat.id, p, reply_markup=markup)
            os.environ["step"] == "attack"
            bot.register_next_step_handler(message, act24, "")

        if number == 2:
            markup.add("сражение ⚔")
            os.environ["en"] = "muravey"
            bot.send_photo(message.chat.id, pic_muravei)
            os.environ["damage_en"] = str(random.randint(5, 12))
            os.environ["en_hp"] = str(random.randint(7, 15))
            p = "ты встретил муравья 🐜(" + os.environ["en_hp"] + "❤️)(" + os.environ["damage_en"] + "⚔)"
            bot.send_message(message.chat.id, p, reply_markup=markup)
            os.environ["step"] == "attack"
            bot.register_next_step_handler(message, act24, "")


    else:
        bot.register_next_step_handler(message, act19, "")
##искать еду


## вопросы

def act20(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if message.text == "ответить":
        number = str(random.randint(1,2))
        question = os.environ["ql_" + number]
        answer = os.environ["ql_" + number + '0']
        option1 = answer
        option2 = os.environ["ql_" + number + '1']
        option3 = os.environ["ql_" + number + '2']
        bot.send_message(message.chat.id, question,reply_markup=markup)
        number = int(random.randint(1,6))
        if number == 1:
             markup.add(option1,option2,option3)
        if number == 2:
             markup.add(option1,option3,option2)
        if number == 3:
             markup.add(option2,option1,option3)
        if number == 4:
             markup.add(option2,option3,option1)
        if number == 5:
             markup.add(option3,option1,option2)
        if number == 6:
             markup.add(option3,option2,option1)
        bot.send_message(message.chat.id, 'реши загадку',reply_markup=markup)
        bot.register_next_step_handler(message, act21,answer)
    else:
        bot.register_next_step_handler(message, act20,"")


## проверка ответа

def act21(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    reply_markup = markup
    why = os.environ["ql_" + right_answer + 'w']


    if message.text == right_answer:
            bot.send_message(message.chat.id, "правильно ✔", reply_markup=markup)
            os.environ["is_answer_right"] = "1"
            os.environ["exp"] = str(int(os.environ["exp"]) + 5)
            exp = int(os.environ["exp"])
            if exp == 200 or exp > 200:
                exp = exp - 200
                os.environ["level"] = str(int(os.environ["level"]) + 1)
            level = os.environ["level"]
            os.environ["exp"] = str(exp)
            level = 'ваш уровень : ' + os.environ["level"]
            bot.send_message(message.chat.id, level, reply_markup=markup)
            exp = 'опыт : ' + os.environ["exp"] + "/200"
            bot.send_message(message.chat.id, exp, reply_markup=markup)


    else:
            markup.add("продолжить")
            bot.send_message(message.chat.id, "неправильно ❌", reply_markup=markup)
            os.environ["is_answer_right"] = "0"
            bot.send_message(message.chat.id, "правильный ответ", reply_markup=markup)
            bot.send_message(message.chat.id, right_answer, reply_markup=markup)
    bot.send_message(message.chat.id, why, reply_markup=markup)
    if os.environ["is_answer_right"] == "1":
        if os.environ["location"] == "les":
            if os.environ["target"] == "eda":
             markup.add("собрать")
             number = int(random.randint(5, 20))+ int(os.environ["laky_f"])
             os.environ["listok"]=str(number + int(os.environ["laky_f"]))
             bot.send_photo(message.chat.id, pic_listok)
             listok = 'ты обноружил листок 🌿(' + str(number) + ")"
             bot.send_message(message.chat.id,listok, reply_markup=markup)
             bot.register_next_step_handler(message, act22, "")
    if os.environ["is_answer_right"] == "0":
     bot.register_next_step_handler(message, act18, "")

def act22(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("продолжить")


    if message.text == "собрать":
     bot.send_message(message.chat.id, 'сбор окончен', reply_markup=markup)
     number = os.environ["listok"]
     sklad = int(number) + int(os.environ["sklad"])
     os.environ["sklad"] = str(sklad)
     if  int(os.environ["sklad"]) >= int(os.environ["sklad_max"]):
       os.environ["sklad"] = str(int(os.environ["sklad"]) - (int(os.environ["sklad"]) - int(os.environ["sklad_max"])))
       bot.send_message(message.chat.id, "❗ склад заполнен ❗", reply_markup=markup)
     sklad = 'склад : ' + os.environ["sklad"] + "🌿/" + os.environ["sklad_max"] + "🌿"
     bot.send_message(message.chat.id,sklad, reply_markup=markup)
     bot.register_next_step_handler(message, act18, "")
    else:
        bot.register_next_step_handler(message, act22, "")

def act23(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("продолжить")

    if message.text == "1⭐":
        if int(os.environ["sklad"]) >= int(os.environ["price_s_f"]):

            os.environ["sklad_max"] = str(int(os.environ["sklad_max"]) + 15)
            os.environ["sklad"] = str(int(os.environ["sklad"]) - int(os.environ["price_s_f"]))
            bot.send_message(message.chat.id, "🎉 улучшение успешно 🎉", reply_markup=markup)
            sklad = "склад : " + os.environ["sklad"] + "🌿/" + os.environ["sklad_max"] + "🌿"
            bot.send_message(message.chat.id, sklad, reply_markup=markup)
            os.environ["price_s_f"] = str(int(os.environ["price_s_f"]) + 10)
            bot.register_next_step_handler(message, act18, "")
        else:
            bot.send_message(message.chat.id, "❗ не хватает средств ❗", reply_markup=markup)
            bot.register_next_step_handler(message, act18, "")

    if message.text == "2⭐":
        if int(os.environ["sklad"]) >= int(os.environ["price_l_f"]):
            os.environ["laky_f"] = str(int(os.environ["laky_f"]) + 2)
            os.environ["sklad"] = str(int(os.environ["sklad"]) - int(os.environ["price_l_f"]))
            bot.send_message(message.chat.id, "🎉 улучшение успешно 🎉", reply_markup=markup)
            sklad = "склад : " + os.environ["sklad"] + "🌿/" + os.environ["sklad_max"] + "🌿"
            bot.send_message(message.chat.id, sklad, reply_markup=markup)
            os.environ["price_l_f"] = str(int(os.environ["price_l_f"]) + 20)
            bot.register_next_step_handler(message, act18, "")
        else:
            bot.send_message(message.chat.id, "❗ не хватает средств ❗", reply_markup=markup)
            bot.register_next_step_handler(message, act18, "")
    if message.text == "3⭐":
        if int(os.environ["sklad"]) >= int(os.environ["price_l_f"]):
            os.environ["hp_max"] = str(int(os.environ["hp_max"]) + 1)
            os.environ["sklad"] = str(int(os.environ["sklad"]) - int(os.environ["price_hp"]))
            bot.send_message(message.chat.id, "🎉 улучшение успешно 🎉", reply_markup=markup)
            sklad = "склад : " + os.environ["sklad"] + "🌿/" + os.environ["sklad_max"] + "🌿"
            bot.send_message(message.chat.id, sklad, reply_markup=markup)
            bot.register_next_step_handler(message, act18, "")
        else:
            bot.send_message(message.chat.id, "❗ не хватает средств ❗", reply_markup=markup)
            bot.register_next_step_handler(message, act18, "")
    else:
        bot.register_next_step_handler(message, act23, "")

def act24(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    number = str(random.randint(3,3))
    question = os.environ["ql_" + number]
    answer = os.environ["ql_" + number + '0']
    option1 = answer
    option2 = os.environ["ql_" + number + '1']
    option3 = os.environ["ql_" + number + '2']
    bot.send_message(message.chat.id, question,reply_markup=markup)
    number = int(random.randint(1,6))
    if number == 1:
             markup.add(option1,option2,option3)
    if number == 2:
             markup.add(option1,option3,option2)
    if number == 3:
             markup.add(option2,option1,option3)
    if number == 4:
             markup.add(option2,option3,option1)
    if number == 5:
             markup.add(option3,option1,option2)
    if number == 6:
             markup.add(option3,option2,option1)
    bot.send_message(message.chat.id, 'реши задачу',reply_markup=markup)
    bot.register_next_step_handler(message, act25,answer)

def act25(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    why = os.environ["ql_" + right_answer + 'w']
    if message.text == right_answer and os.environ["step"] =="attack" :
        markup.add("атаковать ⚔")
        bot.send_message(message.chat.id, 'правильно ✔,ты получаешь возможность атаки', reply_markup=markup)
        os.environ["is_answer_right"] = "1"


    elif message.text == right_answer and os.environ["step"] =="protection" :
        markup.add("защититься 🛡️")
        bot.send_message(message.chat.id, 'правильно ✔,ты получаешь возможность защиты', reply_markup=markup)
        os.environ["is_answer_right"] = "1"

    else:
        markup.add("продолжить")
        bot.send_message(message.chat.id, "неправильно ❌", reply_markup=markup)
        os.environ["is_answer_right"] = "0"
        bot.send_message(message.chat.id, "правильный ответ", reply_markup=markup)
        bot.send_message(message.chat.id, right_answer, reply_markup=markup)
    bot.send_message(message.chat.id, why, reply_markup=markup)
    bot.register_next_step_handler(message, act26, "")

def act26(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if message.text == "атаковать ⚔" and os.environ["is_answer_right"] == "1" and os.environ["step"] =="attack" :
        os.environ["en_hp"] =  str(int(os.environ["en_hp"]) - int(os.environ["damage"]))
        if int(os.environ["en_hp"]) <= 0 :
            os.environ["en_hp"] = "0"
            bot.send_message(message.chat.id, "ты выиграл", reply_markup=markup)
        p = "враг (" + os.environ["en_hp"] + "❤️)"
        hp = "здоровье : " + os.environ["hp"] + "❤️/" + os.environ["hp_max"] + "    " + os.environ["hetin"] + "🛡️/" +  os.environ["hetin_max"] + "🛡️"
        bot.send_message(message.chat.id, p, reply_markup=markup)
        bot.send_message(message.chat.id, hp, reply_markup=markup)
        os.environ["step"] == "protection"
        bot.register_next_step_handler(message, act24, "")

    elif message.text == "продолжить" and os.environ["is_answer_right"] == "0" and os.environ["step"] =="attack" :
        markup.add("продолжить")
        p = "враг (" + os.environ["en_hp"] + "❤️)"
        hp = "здоровье : (" + os.environ["hp"] + "❤️/" + os.environ["hp_max"] + ")    (" + os.environ["hetin"] + "🛡️/" + os.environ["hetin_max"] + "🛡️)"
        bot.send_message(message.chat.id, p, reply_markup=markup)
        bot.send_message(message.chat.id, hp, reply_markup=markup)
        os.environ["step"] == "protection"
        bot.register_next_step_handler(message, act24, "")

    elif message.text == "защититься 🛡️" and os.environ["is_answer_right"] == "1" and os.environ["step"] =="protection" :
        os.environ["hetin"] = str(int(os.environ["hetin"]) - int(os.environ["damage_en"]))
        p = "враг (" + os.environ["en_hp"] + "❤️)"
        if int(os.environ["hetin"]) <= 0 :
            os.environ["hp"] = str(int(os.environ["hp"]) + int(os.environ["hetin"]))
            os.environ["hetin"] = '0'
        if int(os.environ["hp"]) <= 0:
            os.environ["hp"] = "0"
            bot.send_message(message.chat.id, "ты проиграл", reply_markup=markup)
        hp = "здоровье : " + os.environ["hp"] + "❤️/" + os.environ["hp_max"] + "    " + os.environ["hetin"] + "🛡️/" +  os.environ["hetin_max"] + "🛡️"
        bot.send_message(message.chat.id, p, reply_markup=markup)
        bot.send_message(message.chat.id, hp, reply_markup=markup)
        os.environ["step"] == "attack"
        bot.register_next_step_handler(message, act24, "")

    elif message.text == "продолжить" and os.environ["is_answer_right"] == "0" and os.environ["step"] == "protection":
        markup.add("продолжить")
        os.environ["hp"] = str(int(os.environ["hp"]) + int(os.environ["damage_en"]))
        if int(os.environ["hp"]) <= 0:
            bot.send_message(message.chat.id, "ты проиграл", reply_markup=markup)
        bot.send_message(message.chat.id, "kflyj", reply_markup=markup)


    else :
        bot.register_next_step_handler(message, act26, "")


bot.infinity_polling()
