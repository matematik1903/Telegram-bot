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

from telebot import types
from datetime import date
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

print(config.get('TOKEN','telegram-bot'))
bot = telebot.TeleBot(config.get('TOKEN','telegram-bot'))
print("\nToday's date:", date.today())

# init user-employee
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
        df = pd.read_csv("data.csv").append(user, ignore_index = True)
        df.to_csv("data.csv", index=False)
    else:
        print("Error: not find data.csv")



# COMMAND: today
# send questions for answer
@bot.message_handler(commands=["today"])
def today(m, res=False):
    # bot.delete_message(m.chat.id, m.message_id)
    markup1 = types.InlineKeyboardMarkup()
    buttonA1 = types.InlineKeyboardButton('Full-time', callback_data='Full-time')
    buttonB1 = types.InlineKeyboardButton('Part-time', callback_data='Part-time')
    buttonC1 = types.InlineKeyboardButton("Can't Work", callback_data="Can't work")

    markup2 = types.InlineKeyboardMarkup()
    buttonA2 = types.InlineKeyboardButton('0-2', callback_data='0-2')
    buttonB2 = types.InlineKeyboardButton('2-5', callback_data='2-5')
    buttonC2 = types.InlineKeyboardButton("5-7", callback_data="5-7")
    buttonD2 = types.InlineKeyboardButton("8-10", callback_data="8-10")

    markup3 = types.InlineKeyboardMarkup()
    buttonA3 = types.InlineKeyboardButton('Нужна помощь, напишите мне!', callback_data='Нужна помощь, напишите мне!')
    buttonB3 = types.InlineKeyboardButton('Помощь не нужна! Все хорошо', callback_data='Помощь не нужна! Все хорошо')

    markup4 = types.InlineKeyboardMarkup()
    buttonA4 = types.InlineKeyboardButton('За рубежом', callback_data='За рубежом')
    buttonB4 = types.InlineKeyboardButton('Крым', callback_data='Крым')
    buttonC4 = types.InlineKeyboardButton('Винницкая область', callback_data='Винницкая область')
    buttonD4 = types.InlineKeyboardButton("Волынская область", callback_data="Волынская область")
    buttonE4 = types.InlineKeyboardButton("Днепровская область", callback_data="Днепровская область")
    buttonF4 = types.InlineKeyboardButton("Донецкая область", callback_data="Донецкая область")
    buttonG4 = types.InlineKeyboardButton("Житомирская область", callback_data="Житомирская область")
    buttonH4 = types.InlineKeyboardButton("Закарпатская область", callback_data="Закарпатская область")
    buttonI4 = types.InlineKeyboardButton("Запорожская область", callback_data="Запорожская область")
    buttonJ4 = types.InlineKeyboardButton("Ивано-Франковская область", callback_data="Ивано-Франковская область")
    buttonK4 = types.InlineKeyboardButton("Киевская область", callback_data="Киевская область")
    buttonL4 = types.InlineKeyboardButton("Кировоградская область", callback_data="Кировоградская область")
    buttonM4 = types.InlineKeyboardButton("Луганская область", callback_data="Луганская область")
    buttonN4 = types.InlineKeyboardButton("Львовская область", callback_data="Львовская область")
    buttonO4 = types.InlineKeyboardButton("Николаевская область", callback_data="Николаевская область")
    buttonP4 = types.InlineKeyboardButton("Одесская область", callback_data="Одесская область")
    buttonQ4 = types.InlineKeyboardButton("Ровенская область", callback_data="Ровенская область")
    buttonR4 = types.InlineKeyboardButton("Харьковская область", callback_data="Харьковская область")
    buttonS4 = types.InlineKeyboardButton("Херсонская область", callback_data="Херсонская область")
    buttonT4 = types.InlineKeyboardButton("Полтавская область", callback_data="Полтавская область")
    buttonU4 = types.InlineKeyboardButton("Киев", callback_data="Киев")
    buttonV4 = types.InlineKeyboardButton("Сумская область", callback_data="Сумская область")
    buttonW4 = types.InlineKeyboardButton("Тернопольская область", callback_data="Тернопольская область")
    buttonX4 = types.InlineKeyboardButton("Хмельницкая область", callback_data="Хмельницкая область")
    buttonY4 = types.InlineKeyboardButton("Черкасская область", callback_data="Черкасская область")
    buttonZ4 = types.InlineKeyboardButton("Черновицкая область", callback_data="Черновицкая область")
    button44 = types.InlineKeyboardButton("Черниговская область", callback_data="Черниговская область")

    markup4.row(buttonA4, buttonB4, buttonC4)
    markup4.row(buttonD4, buttonE4, buttonF4)
    markup4.row(buttonG4, buttonH4, buttonI4)
    markup4.row(buttonJ4, buttonK4, buttonL4)
    markup4.row(buttonP4, buttonQ4, buttonR4)
    markup4.row(buttonM4, buttonN4, buttonO4)
    markup4.row(buttonS4, buttonT4, buttonU4)
    markup4.row(buttonV4, buttonW4, buttonX4)
    markup4.row(buttonY4, buttonZ4, button44)

    bot.send_message(m.chat.id,
                "Дай, пожалуста, ответы на следущие вопросы")

    bot.send_message(m.chat.id,
                "🔹 1. Можешь ли ты *работать*?",
                parse_mode = telegram.ParseMode.MARKDOWN,
                reply_markup = markup1.row(buttonA1, buttonB1, buttonC1))

    bot.send_message(m.chat.id,
                "🔹 2. Оцените свое *состояние*: ( от 0 к 10 )",
                parse_mode = telegram.ParseMode.MARKDOWN,
                reply_markup = markup2.row(buttonA2, buttonB2, buttonC2, buttonD2))

    bot.send_message(m.chat.id,
                "🔹 3. Необходима ли тебе какая-то орг *помощь*?",
                parse_mode = telegram.ParseMode.MARKDOWN,
                reply_markup = markup3.row(buttonA3).row(buttonB3))

    bot.send_message(m.chat.id,
                "🔹 4. Где ты территориально *находишься*?",
                parse_mode = telegram.ParseMode.MARKDOWN,
                reply_markup = markup4)


# Question: Can you work today?
# SAVE ANSWER
@bot.callback_query_handler(lambda call: True)
def handle(call):
    # MERGE data for answer:
    answer = {'date': date.today(),
              'time':	datetime.now().strftime("%H:%M:%S"),
              'username': call.message.chat.username,
              'event': 'clicks',
              'event_description': call.data,
              'first_name': call.message.chat.first_name,
              'last_name': call.message.chat.last_name,
              'chat_id': call.message.chat.id}

    if(os.path.exists('data.csv') == True):
        df = pd.read_csv("data.csv").append(answer, ignore_index = True)
        df.to_csv("data.csv", index=False)
    else:
        print("Error: not find data.csv")

    reply_to_user = "🔺" + str(date.today()) + " " + str(call.message.text) + " | Вы выбрали: *" + str(call.data) + "*  "
    bot.send_message(call.message.chat.id, reply_to_user,
                     parse_mode = telegram.ParseMode.MARKDOWN)



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
    bot.send_message(message.chat.id, "Твое сообщение передано для обработки дальше. Спасибо, что указываешь детали !")


# run bot
bot.polling(none_stop=True, interval=0)
