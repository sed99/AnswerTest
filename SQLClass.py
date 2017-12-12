import sqlite3

class SQLClass:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_all(self, table):
        """Получаем все строки таблицы"""
        return self.cursor.execute('SELECT * FROM '
                                   + str(table)).fetchall()


    def count_rows(self, table):
        """Считаем количесвто строк в таблице"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM '
                                        + str(table)).fetchall()
            return len(result)

    def select_singl(self, table, col, row):
        """Получаем одну строку из таблицы"""
        with self.connection:
            return self.cursor.execute('SELECT * FROM '
                                       +str(table)+' WHERE '
                                       +str(col) + ' = '
                                       +str(row)).fetchall()[0]

    def add_row(self, table, col, row):
        """Добавляем запись в таблицу"""
        with self.connection:
            self.cursor.execute('INSERT INTO '+str(table)+
                                ' ('+str(col)+') VALUES ('+str(row)+')')
            self.connection.commit()


    def del_row(self,table, col, row, text):
        """Удаляем запись из таблицы"""
        with self.connection:
            self.cursor.execute('DELETE FROM '+str(table)+
                                ' WHERE '+str(col)+' = '+str(row))
            self.connection.commit()


    def change_row(self, table,col,row,text, num):
        """Перезаписываем строку из таблицы"""
        with self.connection:
            self.cursor.execute('UPDATE '+str(table)+
                                ' SET ' +str(col)+
                                ' = '+str(text)+
                                ' WHERE '+str(row)+ ' = ' +str(num))
            self.connection.commit()


    def close(self):
        """Закрывааем сессию с БД"""
        self.connection.close()