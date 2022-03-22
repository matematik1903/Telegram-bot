 # -*- coding: utf-8 -*-

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
import configparser

import today_box

from telebot import types
from datetime import date
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

bot = telebot.TeleBot(config.get('TOKEN','telegram-bot'))
print("\nToday's date:", date.today())

# init user-employee
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id,
                     '✌️ *Привіт* Це S-PRO перекличка.\nХочеться бути на зв’язку з нашою великою українською командою у такий час. \n\nЦей бот буде щодня відправляти тобі чотири питання. Будь ласка, відповідай на них до 12:00, аби HR команда могла оперативно моніторити стан співробітників та, за необхідності, допомогти. \n\nНатискай команду 🔻 /today 🔻 і проходь перекличку сьогодні :)',
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
    print("\ndate:", date.today(), '\ntime ',	datetime.now().strftime("%H:%M:%S"), " | Законектився працівник | ",  m.chat.username)

    if(os.path.exists('data.csv') == True):
        df = pd.read_csv("data.csv").append(user, ignore_index = True)
        df.to_csv("data.csv", index=False)
    else:
        print("Error: not find data.csv")


# COMMAND: today
# send questions for answer
@bot.message_handler(commands=["today"])
def today(m, res=False):
    today_box.today_send(m.chat.id)


# Question: Can you work today?
# SAVE ANSWER
@bot.callback_query_handler(lambda call: True)
def handle(call):
    # MERGE data for answer:
    answer = {'date': date.today(),
              'time':	datetime.now().strftime("%H:%M:%S"),
              'username': call.message.chat.username,
              'event': str(call.message.text),
              'event_description': call.data,
              'first_name': call.message.chat.first_name,
              'last_name': call.message.chat.last_name,
              'chat_id': call.message.chat.id}

    if(os.path.exists('data.csv') == True):
        df = pd.read_csv("data.csv").append(answer, ignore_index = True)
        df.to_csv("data.csv", index=False)
    else:
        print("Error: not find data.csv")

    # reply_to_user = "🔺" + str(date.today()) + " " + str(call.message.text) + " : *" + str(call.data) + "*  "
    reply_to_user = "🔸" + str(date.today()) + " " + str(call.message.text) + " : *" + str(call.data) + "*  "

    bot.send_message(call.message.chat.id, reply_to_user,
                     parse_mode = telegram.ParseMode.MARKDOWN)


@bot.message_handler(commands=["newsletter"])
def answer(message):
    if (message.from_user.id == 809104544):
        # newsletter = '✌️ *Привет*, это пишет бот-помощник HR команди S-PRO | мы тебя нашли в базе работников и сейчас делаем тест утренней рассылки для опроса :). 💭'
        newsletter = '✌️ *Привіт*'
        all_users = pd.read_csv('data.csv')['chat_id'].unique()
        for i in all_users:
            try:
                bot.send_message(i,
                                 newsletter,
                                 parse_mode=telegram.ParseMode.MARKDOWN)
                today_box.today_send(i)
                print("i:", i, " | message send | done ")
            except:
                continue


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
        df = pd.read_csv("data.csv").append(answer_text, ignore_index = True)
        df.to_csv("data.csv", index=False, encoding='utf-8')
    else:
        print("Error: not find data.csv")
    bot.send_message(message.chat.id, "Дякую за твоє повідомлення, я передам його HR команді!")



# run bot
bot.polling(none_stop=True, interval=0)
