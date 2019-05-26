import SQLcommands
from DataTable import DataTable


class DataTableReader(DataTable):
    def __init__(self, dbname, sex):
        DataTable.__init__(self, dbname)
        self.sex = sex

    def avg_participants(self, region, year):
        self.cur.execute(SQLcommands.Commands.get_avg_participants(region, year, self.sex))
        dane = self.cur.fetchall()

        print("1)")
        for dana in dane:
            print(dana[0], dana[1])
        print()
        return dane

    def percentage_passed(self, region):
        self.cur.execute(SQLcommands.Commands.get_percentage_passed(region, self.sex))
        passed = self.cur.fetchall()

        print("2)")
        for p in passed:
            print(p[0], str(int(p[1])) + "%", )
        print()

    def best_region(self, year):
        self.cur.execute(SQLcommands.Commands.get_best_region(year, self.sex))
        best = self.cur.fetchall()

        print("3)")
        for b in best:
            print(b[0], str(int(b[1])) + "%", )
        print()

    def regression_checker(self):
        self.cur.execute(SQLcommands.Commands.get_regression(self.sex))
        result = self.cur.fetchall()

        previous_result = result[0][2]
        previous_region = result[0][1]

        print("4)")
        for reg in result:
            if previous_region != reg[1]:
                previous_result = reg[2]
                previous_region = reg[1]
            if reg[2] < previous_result:
                print(reg[1] + ":", reg[0] + " ->", str(int(reg[0]) - 1))
            previous_result = reg[2]
        print()

    def comparison(self, region1, region2):
        self.cur.execute(SQLcommands.Commands.get_comparison(region1, region2, self.sex))
        results = self.cur.fetchall()

        print("5)")
        for result in results:
            if result[2] > result[4]:
                bigger = result[1]
            else:
                bigger = result[3]
            print(result[0], bigger)
        print()
