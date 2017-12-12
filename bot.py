import telebot
import config
import status
import modules
from telebot import types
from SQLClass import SQLClass



bot = telebot.TeleBot(config.token)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
keyboard.row('Загадать препарат')



@bot.message_handler(commands=['start'])

def new_member(message):
    db = SQLClass(config.db)
    flag = db.del_row(table=config.t_chat,col=config.col_u,row=message.chat.id)
    if flag == None:
        db.add_row(table=config.t_chat,col=config.col_u,row=message.chat.id)
    db.close()
    keyboard.one_time_keyboard = True
    msg = bot.send_message(message.chat.id, 'Начнем', parse_mode='HTML',reply_markup=keyboard)
    bot.register_next_step_handler(msg, new_qwestion)

@bot.message_handler(content_types='text')

def all_answers(message):
    db = SQLClass(config.db)
    res = db.all_qwestins()
    bot.send_message(message.chat.id, res)




if __name__ == '__main__':
    bot.polling(none_stop=True)

