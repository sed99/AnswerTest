import sqlite3

class SQLClass:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def all_qwestins(self):
        with self.connection:
            res = self.cursor.execute('SELECT * FROM answers').fetchall()
            return len(res)



    def close(self):
        """Закрывааем сессию с БД"""
        self.connection.close()