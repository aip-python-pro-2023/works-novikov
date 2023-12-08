import os
from dotenv import load_dotenv
import telebot
from telebot import types

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

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'хорошо ,но что бы все получилось ты должен ответить на вопрос',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'сколько пар лап у муравьев', reply_markup=markup)
        bot.register_next_step_handler(message, act2, "3")

## путешествие

def act2(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == right_answer:
        bot.send_photo(message.chat.id, pic_muravyi)
        bot.send_message(message.chat.id, 'отлично , теперь у тебя есть собственная колония муравьев ',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'для существования твоей колонии нужны ресурсы',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'нажми на кнопку "путешествия" и выбери лес что бы найти еду',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act3, "путешествия 🎒")

## вход в лес

def act3(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("лес 🌲")


    if message.text == right_answer:
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act4, "лес 🌲")

## поиск еды

def act4(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("искать еду 🥪")

    if message.text == right_answer:

        bot.send_photo(message.chat.id, pic_les)
        bot.send_message(message.chat.id, 'хорошо , ты зашел в лес , выбери в возможных действиях "искать еду"',
                         reply_markup=markup)
        bot.send_message(message.chat.id, 'чтобы найти еду нужно ответить на вопрос', reply_markup=markup)
        bot.register_next_step_handler(message, act5, "искать еду 🥪")

## вопрос

def act5(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("2", "3", "4")

    if message.text == right_answer:
     bot.send_message(message.chat.id, 'сколько желудков у одного муравья?', reply_markup=markup)
     bot.register_next_step_handler(message, act6, "2")

## ахождение листка

def act6(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("ускорить сбор (бесплатно)")

    if message.text == right_answer:
        bot.send_photo(message.chat.id, pic_listok)
        bot.send_message(message.chat.id, 'ты обноружил листок 🌿 (15) , прикажи своим муравьям забрать его',
                         reply_markup=markup)
        bot.send_message(message.chat.id,
                         'чтобы забирать ресурсы муравьям необходимо время 🕑 (1 мин)',
                         reply_markup=markup)
        bot.send_message(message.chat.id,
                         'чтобы ускорить сбор ты можешь потратить алмаз 💎 , сейчас это бесплатно',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act8, "ускорить сбор (бесплатно)")

## ускорение сбора

def act8(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == right_answer:
     bot.send_message(message.chat.id, 'сбор окончен', reply_markup=markup)
     bot.send_message(message.chat.id, 'склад : + 15 🌿', reply_markup=markup)
     bot.send_message(message.chat.id, 'хорошо , а теперь вернись в колонию', reply_markup=markup)
     bot.register_next_step_handler(message, act9, "путешествия 🎒")

## путешествие

def act9(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("колония 🏡")


    if message.text == right_answer:
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act10, "колония 🏡")

## нападение

def act10(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("атаковать ⚔")
    bot.send_photo(message.chat.id, pic_pauk)

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'похоже что на тебя напал паук 🕷️ (20 хп), нажми на кнопу чтбы дать ему отпор', reply_markup=markup)
        bot.register_next_step_handler(message, act11, "атаковать ⚔")

## атака

def act11(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("защититься 🛡️")


    if message.text == right_answer:
        bot.send_message(message.chat.id, 'паук 🕷️ (10 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'состояние здоровья (10 хп) , состояние хитина (20 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты нанес пауку удар , теперь его ход , защищайся !', reply_markup=markup)
        bot.register_next_step_handler(message, act12, "защититься 🛡️")

## защита

def act12(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("атаковать ⚔")


    if message.text == right_answer:
        bot.send_message(message.chat.id, 'состояние здоровья (10 хп) , состояние хитина (5 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты выдержал удар , но паук повредил твою хитиновую оболочку , она со временем восстанавливается, '
                                          'но чтобы пополнять запас здоровья нужно вернуться в колонию ', reply_markup=markup)
        bot.send_message(message.chat.id, 'продолжай атаку', reply_markup=markup)
        bot.register_next_step_handler(message, act13, "атаковать ⚔")

## победа

def act13(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'паук 🕷️ (0 хп)', reply_markup=markup)
        bot.send_message(message.chat.id, 'ты одержал победу на врагом , теперь ты можешь спокойно вернуться в колонию', reply_markup=markup)
        bot.register_next_step_handler(message, act14, "путешествия 🎒")
## путешествие


def act14(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("колония 🏡")


    if message.text == right_answer:
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act15, "колония 🏡")

## вход в колонию

def act15(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия 🎒",)

    if message.text == right_answer:
        bot.send_photo(message.chat.id, pic_muravyi)
        bot.send_message(message.chat.id, 'ты вернулся в колонию', reply_markup=markup)
        bot.send_message(message.chat.id, 'здесь ты можешь улучшать свою её и воссотанавливать здоровье  , '
                                          'а сейчас твоё обучение закончино , удачи!', reply_markup=markup)
        bot.register_next_step_handler(message, act16, "")

#################################################################################################
## конец обучения

def act16(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("лес 🌲")


    if message.text == "путешествия 🎒" :
        bot.send_message(message.chat.id, 'выбрери локацию', reply_markup=markup)
        bot.register_next_step_handler(message, act17, "")
##путешествия

def act17(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("искать еду 🥪", "искать врага ⚔")

    if message.text == "лес 🌲":
        bot.send_photo(message.chat.id, pic_les)
        bot.send_message(message.chat.id, 'Ты зашел в лес',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act18, "")

##лес

def act18(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)


    if message.text == "искать еду 🥪" :

        bot.send_message(message.chat.id, 'чтобы найти еду нужно ответить на вопрос',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act19, ".")

   ##искать еду

def act19(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("биология 🔬", "физика 🌈", "химия 🎆", "математика ➗", "геометрия 📐")

    if message.text == "." :
        bot.send_message(message.chat.id, 'выбери тему', reply_markup=markup)
        bot.send_message(message.chat.id, 'чтобы найти еду нужно ответить на вопрос',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act19, "")



bot.infinity_polling()
