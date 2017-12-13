#-*- coding: utf-8 -*-

import sqlite3

class SQLClass:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def all_questions(self):
        """Возращает количество строк в таблице answers"""
        with self.connection:
            res = self.cursor.execute('SELECT * FROM answers').fetchall()
            return len(res)

    def all_users(self):
        """Возращает количесвто строк в таблице users"""
        with self.connection:
            res = self.cursor.execute('SELECT * FROM users').fetchall()
            return len(res)

    def single_question(self, rownum):
        """Возрадает одну строку по номеру из таблицы answers"""
        with self.connection:
            return self.cursor.execute('SELECT * FROM answers '
                                       'WHERE id_question = ?',
                                       (rownum,)).fetchall()

    def single_user(self, chat_id):
        """Возвращает одну строку по номеру из таблицы users"""
        with self.connection:
            return self.cursor.execute('SELECT * FROM users '
                                       'WHERE id_chat = ?',
                                       (chat_id,)).fetchall()

    def add_user(self, chat_id):
        """Записывает нового пользователя в талицу users"""
        with self.connection:
            self.cursor.execute('INSERT INTO users (id_chat)'
                                       'VALUES (?)', (chat_id,))
            self.connection.commit()

    def del_user(self, chat_id):
        """Удаляет пользователя по chat_id из таблицы users"""
        with self.connection:
            self.cursor.execute('DELETE FROM users '
                                'WHERE id_chat = ?',(chat_id,))
            self.connection.commit()

    def in_user(self, chat_id):
        """Проверяет вхождение пользователя по chat_id в таблицу users"""
        with self.connection:
            return self.cursor.execute('SELECT COUNT(id_chat) '
                                'FROM users WHERE id_chat = ?',
                                (chat_id,)).fetchall()

    def change_user(self, chat_id, col, text):
        """Изменяет данные в столбце col пользователя по chat_id в таблице users
        :param chat_id: id чата
        :param col: столбец в который вносим изменение
        :param text: изменненые значения"""
        with  self.connection:
            self.cursor.execute('UPDATE users SET '
                                + str(col)+ ' = ? WHERE id_chat = ?',
                                (text, chat_id,))
            self.connection.commit()

    def close(self):
        """Закрывааем сессию с БД"""
        self.connection.close()
