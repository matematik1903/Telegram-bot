import telebot
import telegram
import os.path
import configparser

from telebot import types

config = configparser.ConfigParser()
config.read('config.ini')

bot = telebot.TeleBot(config.get('TOKEN','telegram-bot'))

def today_send(chat_id):
        # bot.delete_message(m.chat.id, m.message_id)
        markup1 = types.InlineKeyboardMarkup()
        buttonA1 = types.InlineKeyboardButton('Full-time', callback_data='Full-time')
        buttonB1 = types.InlineKeyboardButton('Part-time', callback_data='Part-time')
        buttonC1 = types.InlineKeyboardButton("Не можу працювати", callback_data="Не можу працювати")

        markup2 = types.InlineKeyboardMarkup()
        buttonA2 = types.InlineKeyboardButton("0-2", callback_data="0-2 😟")
        buttonB2 = types.InlineKeyboardButton("2-5", callback_data="2-5 😐")
        buttonC2 = types.InlineKeyboardButton("5-7", callback_data="5-7 🙂")
        buttonD2 = types.InlineKeyboardButton("8-10", callback_data="8-10 🤗")

        markup3 = types.InlineKeyboardMarkup()
        buttonA3 = types.InlineKeyboardButton('Так, напишіть мені', callback_data='Так, напишіть мені')
        buttonB3 = types.InlineKeyboardButton('Ні, все ок', callback_data='Ні, все ок')

        markup4 = types.InlineKeyboardMarkup()
        buttonA4 = types.InlineKeyboardButton('За кордоном', callback_data='За кордоном')
        buttonB4 = types.InlineKeyboardButton("Чернігівська", callback_data="Чернігівська область")
        buttonC4 = types.InlineKeyboardButton('Вінницька', callback_data='Вінницька область')
        buttonD4 = types.InlineKeyboardButton("Волинська", callback_data="Волинська область")
        buttonE4 = types.InlineKeyboardButton("Дніпровська", callback_data="Дніпровська область")
        buttonF4 = types.InlineKeyboardButton("Донецька", callback_data="Донецька область")
        buttonG4 = types.InlineKeyboardButton("Житомирська", callback_data="Житомирська область")
        buttonH4 = types.InlineKeyboardButton("Закарпатська", callback_data="Закарпатська область")
        buttonI4 = types.InlineKeyboardButton("Запорізька", callback_data="Запорізька область")
        buttonJ4 = types.InlineKeyboardButton("Івано-Франківська", callback_data="Івано-Франківська область")
        buttonK4 = types.InlineKeyboardButton("Київська", callback_data="Київська область")
        buttonL4 = types.InlineKeyboardButton("Кіровоградська", callback_data="Кіровоградська область")
        buttonM4 = types.InlineKeyboardButton("Луганська", callback_data="Луганська область")
        buttonN4 = types.InlineKeyboardButton("Львівська", callback_data="Львівська область")
        buttonO4 = types.InlineKeyboardButton("Миколаївська", callback_data="Миколаївська область")
        buttonP4 = types.InlineKeyboardButton("Одеська", callback_data="Одеська область")
        buttonQ4 = types.InlineKeyboardButton("Рівненська", callback_data="Рівненська область")
        buttonR4 = types.InlineKeyboardButton("Харківська", callback_data="Харківська область")
        buttonS4 = types.InlineKeyboardButton("Херсонська", callback_data="Херсонська область")
        buttonT4 = types.InlineKeyboardButton("Полтавська", callback_data="Полтавська область")
        buttonU4 = types.InlineKeyboardButton("м.Київ", callback_data="місто Київ")
        buttonV4 = types.InlineKeyboardButton("Сумська", callback_data="Сумська область")
        buttonW4 = types.InlineKeyboardButton("Тернопільська", callback_data="Тернопільська область")
        buttonX4 = types.InlineKeyboardButton("Хмельницька", callback_data="Хмельницька область")
        buttonY4 = types.InlineKeyboardButton("Черкаська", callback_data="Черкаська область")
        buttonZ4 = types.InlineKeyboardButton("Чернівецька", callback_data="Чернівецька область")


        markup4.row(buttonA4, buttonB4, buttonC4)
        markup4.row(buttonD4, buttonE4, buttonF4)
        markup4.row(buttonG4, buttonH4, buttonI4)
        markup4.row(buttonJ4, buttonK4, buttonL4)
        markup4.row(buttonP4, buttonQ4, buttonR4)
        markup4.row(buttonM4, buttonN4, buttonO4)
        markup4.row(buttonS4, buttonT4, buttonU4)
        markup4.row(buttonV4, buttonW4, buttonX4)
        markup4.row(buttonY4, buttonZ4)

        bot.send_message(chat_id,
                    "✌️ *Як ти, де ти сьогодні*? \n\n_Якщо пальці випадково натисли не на ту відповідь, просто обери знову ту, що потрібно.\n Також можеш написати повідомлення і HR відділ його побачить та обов’язково повернеться до тебе з відповіддю._ ",
                    parse_mode=telegram.ParseMode.MARKDOWN)

        bot.send_message(chat_id,
                    "🔹 1. Сьогодні я *у цій області*:",
                    parse_mode = telegram.ParseMode.MARKDOWN,
                    reply_markup = markup4)

        bot.send_message(chat_id,
                    "🔹 2. Сьогодні *працюю*?",
                    parse_mode = telegram.ParseMode.MARKDOWN,
                    reply_markup = markup1.row(buttonA1, buttonB1, buttonC1))

        bot.send_message(chat_id,
                    "🔹 3. Мій *стан* від 0 до 10 сьогодні: ",
                    parse_mode = telegram.ParseMode.MARKDOWN,
                    reply_markup = markup2.row(buttonA2, buttonB2, buttonC2, buttonD2))

        bot.send_message(chat_id,
                        "🔹 4. Мені потрібна *допомога, порада чи підтримка*?",
                        parse_mode = telegram.ParseMode.MARKDOWN,
                        reply_markup = markup3.row(buttonA3).row(buttonB3))
