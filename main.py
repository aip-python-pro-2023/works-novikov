import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)
pic_pole = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIWI1JEY07dmBler0RKSelI90B77HSxzXhpmenK8R6LHaSNv7afa7XDnxK1UpvJNDKOw0&usqp=CAU"
pic_muravyi = "https://avatars.yandex.net/get-games/1890793/2a000001876b286899c95865b62687ab33d1/pjpg160x160"


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("создать колонию")
    bot.send_message(message.chat.id, 'привет , сейчас ты на поле , нажми на кнопку чтобы создать колонию',
                     reply_markup=markup)
    bot.register_next_step_handler(message, act1, "создать колонию")


def act1(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("2", "3", "4")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'хорошо ,но что бы все получилось ты должен ответить на вопрос',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'сколько пар лап у муравьев', reply_markup=markup)
        bot.register_next_step_handler(message, act2, "3")


def act2(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("путешествия")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'отлично , теперь у тебя есть собственная колония муравьев ',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'для существования твоей колонии нужны ресурсы',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'нажми на кнопку "путешествия" и выбери лес что бы найти еду',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act3, "путешествия")


def act3(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("лес")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'выбери локацию', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, act4, "лес")


def act4(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("искать еду")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'хорошо , теперь ты зашел в лес , выбери в возможных действиях "искать еду"',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'чтобы найти еду нужно ответить на вопрос', reply_markup=markup)
        bot.register_next_step_handler(message, act5, "искать еду")


def act5(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("2", "3", "4")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'сколько желудков у одного муравья?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, act6, "2")


def act6(message, right_answer: str):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("ускорить сбор( - &#128142;)")

    if message.text == right_answer:
        bot.send_message(message.chat.id, 'замечательно , ты обноружил листок , прикажи своим муравьям забрать его',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id,
                         'чтобы забирать ресурсы муравьям необходимо время , чтобы ускорить сбор ты можешь потратить алмаз',
                         reply_markup=markup)
        bot.register_next_step_handler(message, act6, "искать еду")


bot.infinity_polling()
