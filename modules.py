#-*- koding: utf-8 -*-

from random import randint


def random_num(a , b):
    """Возращает одно целое число в диапозоне a-b"""
    return randint(a, b)


def parser_string(res):
    """Возвращает обработанную строку, и разбитую на готовые части"""
    res = str(res)
    res = res[1:len(res) - 1].replace("',", ",").replace(")'", ")").replace(', None', '')
    res = res.replace("Фармакологическое действие: ", "<b>Фармакологическое действие:\n</b>")
    res = res.replace("Показания:", "\n\n<b>Показание:\n</b>")
    res = res.split(", '")
    return res

