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

    if message.text == right_answer:
            bot.send_message(message.chat.id, "правильно ✔", reply_markup=markup)

    else:
            bot.send_message(message.chat.id, "неправильно ❌", reply_markup=markup)
            bot.send_message(message.chat.id, "правильный ответ", reply_markup=markup)
            bot.send_message(message.chat.id, right_answer, reply_markup=markup)