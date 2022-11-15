
import telebot
import requests
from lxml import ethree
import csv
import lxml.html

bot = telebot.TeleBot('5782524388:AAFOhIguUcZaPNKHdN8hLnhKdzSAGTreM_o')

def parse  (url):
    api = requests.get(url)
    three = lxml.html.documentfromstring(api.text)
    bot.send_message(message.chat.id, api(api.text), parse_mode='html')



@bot.message_handler(commands= ['start'])
def start(message):
    mess = f' Привет, <b>{message.from_user.first_name} </b>'
    bot.send_message(message.chat.id, mess , parse_mode='html')






#bot.polling(none_stop=True, interval=0)


