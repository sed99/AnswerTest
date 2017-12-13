#-*- koding: utf-8 -*-

from random import randint


def random_num(a , b):
    """Возращает одно целое число в диапозоне a-b"""
    if a > b:
        return randint(a, b)

def parser_question(res):
    """Возвращает обработанную строку, и разбитую на готовые части"""
    if len(res) != 0:
        res = str(res)
        res = res[2:len(res) - 2].replace("',", ",").replace(")'", ")").replace(', None', '')
        res = res.replace("Фармакологическое действие: ", "<b>Фармакологическое действие:\n</b>")
        res = res.replace("Показания:", "\n\n<b>Показание:\n</b>")
        res = res.split(", '")
        return res

def user_statistic(res, message):
    """Возращает строку статистики пользователя"""
    res = str(res).replace("'", "").split(",")
    if len(res) != 0:
        stat = "<b>Никнейм: </b>" + message.from_user.username + "\n"
        stat = stat + "<b>Награда: </b>" + res[6] + "\n"
        stat = stat + "<b>Правильных ответов: </b>" + res[2] + "\n"
        return stat

def full_user_statistic(res, message):
    """Возвращает строку с полной статистикой пользоватея"""
    res = str(res).replace("'", "").split(",")
    if len(res) != 0:
        stat = "<b>Имя: </b>" + message.from_user.username + "\n"
        stat = stat + "<b>Награда: </b>" + res[6] + "\n"
        stat = stat + "<b>Правильных ответов: </b>" + res[2] + "\n"
        stat = stat + "<b>Неправильных ответов: </b>" + res[3] + "\n"
        stat = stat + "<b>Использованно подсказок: </b>" + res[4] + "\n"
        return stat