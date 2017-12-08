import sqlite3

class SQLClass:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_all(self, table):
        """Получаем все строки таблицы"""
        return self.cursor.execute('SELECT * FROM '+ str(table)).fetchall()


    def count_rows(self, table):
        """Считаем количесвто строк в таблице"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM ' + str(table)).fetchall()
            return len(result)

    def select_singl(self, table, id, rownum):
        """Получаем одну строку из таблицы"""
        with self.connection:
            return self.cursor.execute('SELECT * FROM '+str(table)+' WHERE ' +str(id) + ' = ' +str(rownum)).fetchall()[0]

    def add_user(self, table, id):
        with self.connection:
            self.cursor.execute('INSERT INTO '+str(table)+' (id_chat) VALUES ('+str(id)+')')

    def close(self):
        """Закрывааем сессию с БД"""
        self.connection.close()