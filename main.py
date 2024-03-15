import os
from dotenv import load_dotenv
import telebot
from telebot import types
import random


load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)
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
        bot.send_message(message.chat.id, 'уровень 1 опыт 5', reply_markup=markup)
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
        bot.send_message(message.chat.id, 'похоже что на тебя напал паук 🕷️ (20 хп), чтобы его атаковать тебе нужно получить ход, для этотго ответь на вопрос', reply_markup=markup)
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
        bot.send_message(message.chat.id, 'паук 🕷️ (10 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'состояние здоровья (10 хп) , состояние хитина (20 хп)', reply_markup=markup)
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
        bot.send_message(message.chat.id, 'состояние здоровья (10 хп) , состояние хитина (5 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты выдержал удар , но паук повредил твою хитиновую оболочку , она со временем восстанавливается, '
                                          'но чтобы пополнять запас здоровья нужно вернуться в колонию ', reply_markup=markup)
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
        bot.send_message(message.chat.id, 'паук 🕷️ (0 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты одержал победу на врагом , теперь ты можешь спокойно вернуться в колонию', reply_markup=markup)
        bot.send_message(message.chat.id, 'уровень 1 опыт 20', reply_markup=markup)
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
        bot.send_message(message.chat.id, 'сейчас твоё обучение закончино , удачи!', reply_markup=markup)
        os.environ["location"] = "kolonya"
        os.environ["r"] = "2"
        bot.register_next_step_handler(message, act17, "")
    else:
        bot.register_next_step_handler(message, act16, "")

## вход в колонию



def act17(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    if ((os.environ["location"] == "les") or (message.text == "лес 🌲")) and (os.environ["r"] == "1"):
        markup.add("искать еду 🥪", "искать врага ⚔","путешествия 🎒")
        os.environ["location"] = "les"
        if message.text == "лес 🌲":
          bot.send_photo(message.chat.id, pic_les)
          bot.send_message(message.chat.id, 'Ты зашел в лес', reply_markup=markup)

        bot.register_next_step_handler(message, act18, "")

    elif  ((os.environ["location"] == "kolonya") or (message.text == "колония 🏡"))and(os.environ["r"] == "2") :
        markup.add("улучшить колонию ⭐","путешествия 🎒")
        os.environ["location"] = "kolonya"
        if message.text == "колония 🏡":
          bot.send_photo(message.chat.id, pic_muravyi)
          bot.send_message(message.chat.id, 'Ты вернулся в колонию', reply_markup=markup)

        bot.register_next_step_handler(message, act18, "")
    else:
        bot.register_next_step_handler(message, act17, "")
##лес

def act18(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    if message.text == "путешествия 🎒" :
        if os.environ["location"] != "les":
            markup.add("лес 🌲")
            os.environ["r"] = "1"
        if os.environ["location"] != "kolonya":
            markup.add("колония 🏡")
            os.environ["r"] = "2"
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act17, "")

    elif message.text == "искать еду 🥪" :
        markup.add("ответить")
        os.environ["target"] = "eda"
        bot.send_message(message.chat.id, 'чтобы найти еду нужно решить задачу', reply_markup=markup)
        bot.register_next_step_handler(message, act19, "")

    elif message.text == "улучшить колонию ⭐":
        markup.add("1")
        bot.send_message(message.chat.id, 'список возможных улучшений:', reply_markup=markup)
        bot.send_message(message.chat.id, '1) + макс. склад 🌿 до 45 (30 🌿)', reply_markup=markup)
    else:
        bot.register_next_step_handler(message, act18, "")
##искать еду


## вопросы

def act19(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if message.text == "ответить":
        number = str(random.randint(2,3))
        os.environ["number"] = str(number)
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
        bot.register_next_step_handler(message, act20,'')
    else:
        bot.register_next_step_handler(message, act19,"")


## проверка ответа

def act20(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    reply_markup = markup
    number = os.environ["number"]
    answer = os.environ["ql_" + number + '0']
    why = os.environ["ql_" + number + 'w']

    if message.text == answer:
            bot.send_message(message.chat.id, "правильно ✔", reply_markup=markup)
            os.environ["is_answer_right"] = "1"
            os.environ["exp"] = str(int(os.environ["exp"]) + 5)
            exp = int(os.environ["exp"])
            if exp == 200 or exp > 200:
                exp = exp - 200
                os.environ["level"] = str(int(os.environ["level"]) + 1)
            level = os.environ["level"]
            os.environ["exp"] = str(exp)
            bot.send_message(message.chat.id, "уровень :", reply_markup=markup)
            bot.send_message(message.chat.id, level, reply_markup=markup)
            bot.send_message(message.chat.id, "опыт :", reply_markup=markup)
            bot.send_message(message.chat.id, exp, reply_markup=markup)


    else:

            bot.send_message(message.chat.id, "неправильно ❌", reply_markup=markup)
            os.environ["is_answer_right"] = "0"
            bot.send_message(message.chat.id, "правильный ответ", reply_markup=markup)
            bot.send_message(message.chat.id, answer, reply_markup=markup)
    bot.send_message(message.chat.id, why, reply_markup=markup)
    if os.environ["is_answer_right"] == "1":
        if os.environ["location"] == "les":
            if os.environ["target"] == "eda":
             markup.add("собрать")
             number = int(random.randint(5, 20))
             os.environ["listok"]=str(number)
             bot.send_photo(message.chat.id, pic_listok)
             bot.send_message(message.chat.id, 'ты обноружил листок 🌿', reply_markup=markup)
             bot.send_message(message.chat.id,number, reply_markup=markup)
             bot.register_next_step_handler(message, act21, "")
    if os.environ["is_answer_right"] == "0":
     markup.add("продолжить")
     bot.register_next_step_handler(message, act17, "")

def act21(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("продолжить")


    if message.text == "собрать":
     bot.send_message(message.chat.id, 'сбор окончен', reply_markup=markup)
     bot.send_message(message.chat.id, 'склад :', reply_markup=markup)
     number = os.environ["listok"]
     sklad = int(number) + int(os.environ["sklad"])
     os.environ["sklad"] = str(sklad)
     bot.send_message(message.chat.id,sklad, reply_markup=markup)
     bot.register_next_step_handler(message, act17, "")
    else:
        bot.register_next_step_handler(message, act21, "")

bot.infinity_polling()