# QUESTION:
#  Нам нужны вопросы:
#  1. Где ты территориально находишься?
#  2. Оцените свое состояние ?
#  3. Можешь ли ты работать ( фулл/парт/нет)?
#  4. Необходима ли тебе какая-то орг помощь?

# Import Library
import telegram
import telebot
import pandas as pd

import os.path

from telebot import types
from datetime import date
from datetime import datetime


bot = telebot.TeleBot("your token")

print("\nToday's date:", date.today())


# init user-employee ☑️
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id,
                     '✌️ *Привет*, наш помощник-бот позволяет быстро реагировать на разные ситуации. 💭 \n  Для того, чтобы подать нам за сегодня информацию о твоем состояние, нажимай команду 🔻 /today 🔻',
                     parse_mode=telegram.ParseMode.MARKDOWN)

    user = {'date': date.today(),
              'time':	datetime.now().strftime("%H:%M:%S"),
              'username': m.chat.username,
              'event': 'connect',
              'event_description': 'done',
              'first_name': m.chat.first_name,
              'last_name': m.chat.last_name,
              'chat_id': m.chat.id}

    # Show new connection:
    print("\ndate:", date.today(), " | Законектився працівник | ",  m.chat.username)

    if(os.path.exists('data.csv') == True):
        pd.read_csv("data.csv").append(user, ignore_index = True).to_csv("data.csv", index=False)
    else:
        print("Error: not find data.csv")

    # if(os.path.exists('user_connected.csv') == True):
    #    pd.read_csv("user_connected.csv").append(user, ignore_index = True).to_csv("user_connected.csv", index=False)
    # else:
        # print("Error: not find user_connected.csv")
        # pd.DataFrame(data=user).to_csv("user_connected.csv", index=False)


# COMMAND: today ☑️
# send questions for answer
@bot.message_handler(commands=["today"])
def today(m, res=False):
    # bot.delete_message(m.chat.id, m.message_id)
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('Full-time', callback_data='full-time')
    buttonB = types.InlineKeyboardButton('Part-time', callback_data='part-time')
    buttonC = types.InlineKeyboardButton("Can't Work", callback_data="can't work")

    markup.row(buttonA, buttonB, buttonC)

    bot.send_message(m.chat.id,
                "Дай, пожалуста, ответы на следущие вопросы \n 🔹 1. Где ты территориально *находишься*? \n 🔹 2. Оцените свое *состояние* ? ( от 0 к 10 ) \n 🔹 3. Необходима ли тебе какая-то орг *помощь*?",
                parse_mode=telegram.ParseMode.MARKDOWN,
                reply_markup=markup)


# Question: Can you work today? ☑️
# SAVE ANSWER
@bot.callback_query_handler(lambda call: True)
def handle(call):
    # MERGE data for answer:
    answer = {'date': date.today(),
              'time':	datetime.now().strftime("%H:%M:%S"),
              'username': call.message.chat.username,
              'event': 'typework',
              'event_description': call.data,
              'first_name': call.message.chat.first_name,
              'last_name': call.message.chat.last_name,
              'chat_id': call.message.chat.id}

    if(os.path.exists('data.csv') == True):
        pd.read_csv("data.csv").append(answer, ignore_index = True).to_csv("data.csv", index=False)
    else:
        print("Error: not find data.csv")

    # if(os.path.exists('typework.csv') == True):
        # pd.read_csv("typework.csv").append(answer, ignore_index = True).to_csv("typework.csv", index=False)
    # else:
        # print("Error: not find typework.csv")
        # pd.DataFrame(data=answer).to_csv("type_work_dataset.csv", index=False)


# Reply to user-employee answer:
@bot.message_handler(content_types=['text'])
def read_text(message):
    txt = message.text
    print("\n", date.today(), " ", datetime.now().strftime("%H:%M:%S"))
    print(message.chat.username, " ", " | Answer:")
    print(txt)

    answer_text = {'date': date.today(),
                   'time':	datetime.now().strftime("%H:%M:%S"),
                   'username': message.chat.username,
                   'event': 'message',
                   'event_description': txt,
                   'first_name': message.chat.first_name,
                   'last_name': message.chat.last_name,
                   'chat_id': message.chat.id }

    if(os.path.exists('data.csv') == True):
        pd.read_csv("data.csv").append(answer_text, ignore_index = True).to_csv("data.csv", index=False, encoding='utf-8')
    else:
        print("Error: not find data.csv")

    # if(os.path.exists('messages.csv') == True):
    #    pd.read_csv("messages.csv").append(answer_text, ignore_index = True).to_csv("messages.csv", index=False, encoding='utf-8')
    # else:
        # print("Error: not find messages.csv")
        # pd.DataFrame(data=answer_text).to_csv("messages.csv", index=False)

    bot.send_message(message.chat.id, "Спасибо за твой ответ")


# run bot
bot.polling(none_stop=True, interval=0)
