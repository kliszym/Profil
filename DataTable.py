import sqlite3


class DataTable:
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()
