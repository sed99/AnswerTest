#-*- koding: utf-8 -*-

import telebot
import config
import status
import modules
from telebot import types
from SQLClass import SQLClass



bot = telebot.TeleBot(config.token)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
keyboard.row('Загадать препарат')






if __name__ == '__main__':
    bot.polling(none_stop=True)

