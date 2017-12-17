#-*- coding: utf-8 -*-

import psycopg2

class SQLClass:

    def __init__(self, username, password, database):
        self.connection = psycopg2.connect(user=username,
                                           password=password,
                                           dbname=database)
        self.cursor = self.connection.cursor()


    def all_questions(self):
        """Возращает количество строк в таблице answers"""
        with self.connection:
            self.cursor.execute('SELECT count(*) FROM answers;')
            return self.cursor.fetchall()

    def all_users(self):
        """Возращает количесвто строк в таблице users"""
        with self.connection:
            self.cursor.execute('SELECT count(*) FROM users;')
            return self.cursor.fetchall()

    def single_question(self, rownum):
        """Возрадает одну строку по номеру из таблицы answers"""
        with self.connection:
            self.cursor.execute('SELECT * FROM answers '
                                       'WHERE id_question = %s;',
                                       (rownum,))
            return self.cursor.fetchall()

    def single_user(self, chat_id):
        """Возвращает одну строку по номеру из таблицы users"""
        with self.connection:
            self.cursor.execute('SELECT * FROM users '
                                       'WHERE id_chat = %s;',
                                       (chat_id,))
            return self.cursor.fetchall()

    def add_user(self, chat_id):
        """Записывает нового пользователя в талицу users"""
        with self.connection:
            self.cursor.execute('INSERT INTO users (id_chat)'
                                       'VALUES (%s);', (chat_id,))
            self.connection.commit()

    def del_user(self, chat_id):
        """Удаляет пользователя по chat_id из таблицы users"""
        with self.connection:
            self.cursor.execute('DELETE FROM users '
                                'WHERE id_chat = %s;',(chat_id,))
            self.connection.commit()

    def in_user(self, chat_id):
        """Проверяет вхождение пользователя по chat_id в таблицу users"""
        with self.connection:
            self.cursor.execute('SELECT COUNT(id_chat) '
                                'FROM users WHERE id_chat = %s;',
                                (chat_id,))
            return self.cursor.fetchall()

    def change_user(self, chat_id, col, text):
        """Изменяет данные в столбце col пользователя по chat_id в таблице users
        :param chat_id: id чата
        :param col: столбец в который вносим изменение
        :param text: изменненые значения"""
        with self.connection:
            self.cursor.execute('UPDATE users SET '
                                + str(col)+ ' = %s WHERE id_chat = %s;',
                                (text, chat_id,))
            self.connection.commit()

    def close(self):
        """Закрывааем сессию с БД"""
        self.connection.close()
