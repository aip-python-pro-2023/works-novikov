import os
from dotenv import load_dotenv
import telebot
from telebot import types
import random
import time

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)
pic_pole = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIWI1JEY07dmBler0RKSelI90B77HSxzXhpmenK8R6LHaSNv7afa7XDnxK1UpvJNDKOw0&usqp=CAU"
pic_muravyi = "https://avatars.yandex.net/get-games/1890793/2a000001876b286899c95865b62687ab33d1/pjpg160x160"
pic_les = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX1YgDDzzat1aVE6hYtJCCQugHEB8z-PX2ww&usqp=CAU"
pic_listok= "https://img.freepik.com/premium-vector/leaf-logo-icon-in-pixel-art_588783-270.jpg"
pic_pauk="https://static.vecteezy.com/system/resources/previews/023/685/239/original/pixel-art-illustration-spider-pixelated-spider-insect-creepy-enemy-spider-pixelated-for-the-pixel-art-game-and-icon-for-website-and-video-game-old-school-retro-vector.jpg"

## начало обучения
#################################################################################################

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
    markup.add("ускорить сбор (бесплатно)")

    if message.text == "2":
        bot.send_photo(message.chat.id, pic_listok)
        bot.send_message(message.chat.id, 'ты обноружил листок 🌿 (15) , прикажи своим муравьям забрать его',
                         reply_markup=markup)
        bot.send_message(message.chat.id,
                         'чтобы забирать ресурсы муравьям необходимо время 🕑 (1 мин)',
                         reply_markup=markup)
        bot.send_message(message.chat.id,
                         'чтобы ускорить сбор ты можешь потратить алмаз 💎 , сейчас это бесплатно',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act7, "")
    else:
        bot.register_next_step_handler(message, act6, "")

## ускорение сбора

def act7(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == "ускорить сбор (бесплатно)":
     bot.send_message(message.chat.id, 'сбор окончен', reply_markup=markup)
     bot.send_message(message.chat.id, 'склад : + 15 🌿', reply_markup=markup)
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
    markup.add("атаковать ⚔")


    if message.text == "колония 🏡":
        bot.send_photo(message.chat.id, pic_pauk)
        bot.send_message(message.chat.id, 'похоже что на тебя напал паук 🕷️ (20 хп), нажми на кнопу чтбы дать ему отпор', reply_markup=markup)
        bot.register_next_step_handler(message, act10, "")
    else:
        bot.register_next_step_handler(message, act9, "")

## атака

def act10(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("защититься 🛡️")


    if message.text == "атаковать ⚔":
        bot.send_message(message.chat.id, 'паук 🕷️ (10 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'состояние здоровья (10 хп) , состояние хитина (20 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты нанес пауку удар , теперь его ход , защищайся !', reply_markup=markup)
        bot.register_next_step_handler(message, act11, "")
    else:
        bot.register_next_step_handler(message, act10, "")

## защита

def act11(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("атаковать ⚔")


    if message.text == "защититься 🛡️":
        bot.send_message(message.chat.id, 'состояние здоровья (10 хп) , состояние хитина (5 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты выдержал удар , но паук повредил твою хитиновую оболочку , она со временем восстанавливается, '
                                          'но чтобы пополнять запас здоровья нужно вернуться в колонию ', reply_markup=markup)
        bot.send_message(message.chat.id, 'продолжай атаку', reply_markup=markup)
        bot.register_next_step_handler(message, act12, "")
    else:
        bot.register_next_step_handler(message, act11, "")

## победа

def act12(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == "атаковать ⚔":
        bot.send_message(message.chat.id, 'паук 🕷️ (0 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты одержал победу на врагом , теперь ты можешь спокойно вернуться в колонию', reply_markup=markup)
        bot.register_next_step_handler(message, act13, "")
    else:
        bot.register_next_step_handler(message, act12, "")
## путешествие


def act13(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("колония 🏡")


    if message.text == "путешествия 🎒":
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act14, "")
    else:
        bot.register_next_step_handler(message, act13, "")

## вход в колонию

def act14(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == "колония 🏡":
        bot.send_photo(message.chat.id, pic_muravyi)
        bot.send_message(message.chat.id, 'ты вернулся в колонию', reply_markup=markup)
        bot.send_message(message.chat.id, 'здесь ты можешь улучшать свою её и воссотанавливать здоровье  , '
                                          'а сейчас твоё обучение закончино , удачи!', reply_markup=markup)
        bot.register_next_step_handler(message, act15, "")
    else:
        bot.register_next_step_handler(message, act14, "")

#################################################################################################
## конец обучения

def act15(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("лес 🌲")


    if message.text == "путешествия 🎒" :
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act16, "")
    else:
        bot.register_next_step_handler(message, act15, "")
##путешествия

def act16(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("искать еду 🥪", "искать врага ⚔")

    if message.text == "лес 🌲" or "вернуться  ⬅":
        bot.send_photo(message.chat.id, pic_les)
        bot.send_message(message.chat.id, 'Ты зашел в лес',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act17, "")
    else:
        bot.register_next_step_handler(message, act16, "")

##лес

def act17(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("ответить","вернуться  ⬅")

    if message.text == "искать еду 🥪" :

        bot.send_message(message.chat.id, 'чтобы найти еду нужно ответить на вопрос',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act18, "")
    else:
        bot.register_next_step_handler(message, act17, "")

   ##искать еду

def act18(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("случайное ❔ ","биология 🔬", "физика 🌈", "химия 🎆", "математика ➗", "геометрия 📐")

    if message.text == "ответить":
       bot.send_message(message.chat.id, 'выбери тему', reply_markup=markup)
       bot.register_next_step_handler(message, act19, "")
    if message.text == "вернуться  ⬅":
       bot.register_next_step_handler(message, act16, "")
    else:
        bot.register_next_step_handler(message, act18, "")

## вопросы

def act19(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)


    if message.text == "биология 🔬":
        number = str(random.randint(1,1))
    question = os.environ[number]
    answer = os.environ[number + '0']
    option1 = os.environ[number + '1']
    option2 = os.environ[number + '2']
    option3 = os.environ[number + '3']
    markup.add(option1,option2,option3)
    bot.send_message(message.chat.id, question, reply_markup=markup)
    bot.register_next_step_handler(message, act20,answer)

## проверка ответа

def act20(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    ans_time = int(os.environ[right_answer + 't'])
    sec = 0
    ans = 0
    for sec in range(20):
        if message.text == right_answer:
            bot.send_message(message.chat.id, "правильно ✔", reply_markup=markup)
            ans = 1
            sec = 19

        else:
            bot.send_message(message.chat.id, "неправильно ❌", reply_markup=markup)
            bot.send_message(message.chat.id, "правильный ответ", reply_markup=markup)
            bot.send_message(message.chat.id, right_answer, reply_markup=markup)
            ans = 1
            sec = 19

        if sec == 19:
            break
        time.sleep(1)

    if ans == 0:
        bot.send_message(message.chat.id, "время закончилось 🕑", reply_markup=markup)
        bot.send_message(message.chat.id, "правильный ответ", reply_markup=markup)
        bot.send_message(message.chat.id, right_answer, reply_markup=markup)
    bot.register_next_step_handler(message, act19, "")





bot.infinity_polling()
