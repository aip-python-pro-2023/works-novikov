import os
from dotenv import load_dotenv
import telebot
from telebot import types
load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)
pic_pole="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIWI1JEY07dmBler0RKSelI90B77HSxzXhpmenK8R6LHaSNv7afa7XDnxK1UpvJNDKOw0&usqp=CAU"
pic_muravyi="https://avatars.yandex.net/get-games/1890793/2a000001876b286899c95865b62687ab33d1/pjpg160x160"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("создать колонию")
    markup.add(btn1)
    bot.send_photo(message.chat.id, pic_pole)
    bot.send_message(message.chat.id,
                     text="Привет, сейчас ты находишься на поле , нажми на кнопку чтобы создать колнию".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "создать колонию"):
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'хорошо', reply_markup=a)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("2")
        btn2 = types.KeyboardButton("3")
        btn3 = types.KeyboardButton("4")
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,
                         text="для создания колонии тебе нужно ответить на вопрос: сколько пар лап у муравьёв? У тебя есть варианты ответа".format(
                             message.from_user), reply_markup=markup)




bot.infinity_polling()