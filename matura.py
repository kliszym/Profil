import requests
from DataTable import DataTable


class DataTableCreator(DataTable):

    def create_table_command(self, headers):
        command = "CREATE TABLE IF NOT EXISTS matury ("
        command += "id INTEGER PRIMARY KEY ASC"
        for header in headers:
            command += ", " + "\"" + header.strip() + "\"" " varchar(250) NOT NULL"
        command += ")"
        return command

    def insert_command(self, row):
        command = "INSERT INTO matury VALUES(NULL,?"
        for i in range(1, len(row)):
            command += ",?"
        command += ");"
        return command

    def define_columns(self, headers):
        self.cur.execute("DROP TABLE IF EXISTS matury;")
        command = self.create_table_command(headers)
        self.cur.execute(command)

    def add_row(self, row, command):
        self.cur.execute(command, row)
        self.con.commit()

    def read_row(self, line):
        if line == "":
            return None
        return line.split(";")

    def parse_text(self, text):
        lines = text.split('\n')
        line = lines[0]
        headers = self.read_row(line)
        if headers is None:
            return
        self.define_columns(headers)
        command = self.insert_command(headers)
        for line in lines[1:]:
            row = self.read_row(line)
            if row is None:
                return
            self.add_row(row, command)


class Downloader:
    def __init__(self, url):
        self.url = url
        self.result = requests.get(self.url)
        self.result.encoding = 'Windows-1250'

    def get_text(self):
        return self.result.text


d = Downloader("https://www.dane.gov.pl/media/resources/20190520/Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv")
dtc = DataTableCreator("matury.db")
dtc.parse_text(d.get_text())
