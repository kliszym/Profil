import pytest
from DataTableReader import DataTableReader

@pytest.fixture(scope="module")
def test_db():
    import sqlite3
    con = sqlite3.connect("tests.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS matury;")
    cur.execute("""CREATE TABLE IF NOT EXISTS matury (
                    id INTEGER PRIMARY KEY ASC,
                    'Terytorium' varchar(250) NOT NULL,
                    'Przystąpiło/zdało' varchar(250) NOT NULL,
                    'Płeć' varchar(250) NOT NULL,
                    'Rok' INTEGER NOT NULL,
                    'Liczba osób' INTEGER NOT NULL)
                """)

    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'przystąpiło', 'kobiety', 2010, 2000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'zdało', 'kobiety', 2010, 3000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'przystąpiło', 'mężczyźni', 2010, 4000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'zdało', 'mężczyźni', 2010, 5000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'przystąpiło', 'kobiety', 2010, 100))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'zdało', 'kobiety', 2010, 150))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'przystąpiło', 'mężczyźni', 2010, 200))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'zdało', 'mężczyźni', 2010, 250))

    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'przystąpiło', 'kobiety', 2011, 200))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'zdało', 'kobiety', 2011, 300))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'przystąpiło', 'mężczyźni', 2011, 400))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'zdało', 'mężczyźni', 2011, 500))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'przystąpiło', 'kobiety', 2011, 1000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'zdało', 'kobiety', 2011, 1500))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'przystąpiło', 'mężczyźni', 2011, 2000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'zdało', 'mężczyźni', 2011, 2500))

    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'przystąpiło', 'kobiety', 2012, 200))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'zdało', 'kobiety', 2012, 300))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'przystąpiło', 'mężczyźni', 2012, 400))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Polska', 'zdało', 'mężczyźni', 2012, 500))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'przystąpiło', 'kobiety', 2012, 1000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'zdało', 'kobiety', 2012, 1500))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'przystąpiło', 'mężczyźni', 2012, 2000))
    cur.execute("""INSERT INTO matury VALUES (NULL, ?, ?, ?, ?, ?)""", ('Mazowieckie', 'zdało', 'mężczyźni', 2012, 2500))

    con.commit()

    con.close()


def test_dtr(test_db):

#1)
    dtr = DataTableReader('tests.db', None)
    result = dtr.avg_participants('Polska', '2010')
    for dana in result:
        assert dana[0] == 2010
        assert dana[1] == 14000

    dtr.sex = True
    result = dtr.avg_participants('Mazowieckie', '2011')
    for dana in result:
        assert dana[0] == 2011
        assert dana[1] == 1375

    dtr.sex = False
    result = dtr.avg_participants('Polska', '2012')
    for dana in result:
        assert dana[0] == 2012
        assert dana[1] == 3600