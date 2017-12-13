#-*- koding: utf-8 -*-

import telebot
import config
import status
import modules
from telebot import types
from SQLClass import SQLClass



bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=['start'])

def start_chat(message):
    db = SQLClass(config.db)
    flag = db.in_user(message.chat.id)
    flag = str(flag).replace('[(','').replace(',)]','')
    flag = int(flag)
    if flag > 0:
        db.del_user(chat_id=message.chat.id)
        flag = 0
    db.add_user(message.chat.id)
    db.close()







if __name__ == '__main__':
    bot.polling(none_stop=True)

