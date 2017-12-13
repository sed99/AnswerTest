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

    keyboard_question = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True)
    keyboard_question.row('Новый вопрос','Достижения')
    bot.send_message(message.chat.id,
                     'Для начала нажмите кнопку: <b>Новый вопрос</b>',
                     parse_mode="HTML",
                     reply_markup=keyboard_question)


@bot.message_handler(func=lambda message: message.text == u'Новый вопрос')

def question(message):
    db = SQLClass(config.db)
    rownum = modules.random_num(1,97)
    res = db.single_question(rownum=rownum)
    res = modules.parser_question(res=res)

    db.change_user(chat_id=message.chat.id,col='answer_now',text=res[2])
    if len(res) == 4:
        db.change_user(chat_id=message.chat.id, col='commit_answer', text=res[3])
    else:
        db.change_user(chat_id=message.chat.id, col='commit_answer', text='')
    db.close()
    keyboard_answer = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True)
    keyboard_answer.row('Показать ответ','Достижения')


    if len(res[1]) < 4001:
        bot.send_message(message.chat.id,
                     res[1],
                     reply_markup=keyboard_answer,
                     parse_mode="HTML")
    else:
        res_buff = res[1]
        flag = res_buff.rfind("\n\n<b>Показание:\n</b>")
        res1 = res_buff[:flag]
        res2 = res_buff[flag:]
        for s in (res1, res2):
            bot.send_message(message.chat.id,
                             s,
                             reply_markup=keyboard_answer,
                             parse_mode="HTML")


@bot.message_handler(func = lambda message: message.text == u'Достижения')

def achievement(message):
    db = SQLClass(config.db)
    res = db.single_user(message.chat.id)
    bot.send_message(message.chat.id,
                     modules.full_user_statistic(res,message),
                     parse_mode="HTML")

@bot.message_handler(func= lambda message: message.text == u'Показать ответ')

def tooltip(message):
    db = SQLClass(config.db)
    res = db.single_user(message.chat.id)
    answ = modules.tooltip_answer(res)
    tooltip = db.single_user(message.chat.id)
    tooltip = modules.parser_user(tooltip)
    tooltip_sum = int(tooltip[4]) + 1
    db.change_user(chat_id=message.chat.id,
                   col='tool_tip',
                   text = tooltip_sum)
    db.close()
    keyboard_question = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                  one_time_keyboard=True)
    keyboard_question.row('Новый вопрос','Достижения')
    bot.send_message(message.chat.id,
                     answ,
                     reply_markup=keyboard_question,
                     parse_mode="HTML")





if __name__ == '__main__':
    bot.polling(none_stop=True)

