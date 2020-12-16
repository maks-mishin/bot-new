import requests
import telebot
from telebot import types

bot = telebot.TeleBot('1420563097:AAGTcqyz7BZ2eKAirpCYYa7DOjWEBKKuspA')

keyboard = types.InlineKeyboardMarkup()

key_news_polit = types.InlineKeyboardButton(text='Новости мира', callback_data='polit')
keyboard.add(key_news_polit)

key_news_covid = types.InlineKeyboardButton(text='Статистика COVID', callback_data='covid')
keyboard.add(key_news_covid)

key_news_it = types.InlineKeyboardButton(text='IT новости', callback_data='it')
keyboard.add(key_news_it)

key_open_youtube = types.InlineKeyboardButton(text='Ютубчик', callback_data='youtube')
keyboard.add(key_open_youtube)

key_weather = types.InlineKeyboardButton(text='Погода за окном', callback_data='weather')
keyboard.add(key_weather)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'youtube':
        bot.send_message(call.message.chat.id, "https://www.youtube.com/")
    elif call.data == 'weather':
        weather = requests.get('https://wttr.in/Sarov?format=3').text
        bot.send_message(call.message.chat.id, weather)
    else:
        bot.send_message(call.message.chat.id, "Это было демо период. Дальше плати.")


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я бот-телебот.")
        bot.send_message(message.from_user.id, "Что тебе надо?", reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")


bot.polling(none_stop=True, interval=0)
