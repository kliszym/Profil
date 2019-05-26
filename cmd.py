from DataTableReader import DataTableReader
import sys


class CmdInterface:

    def __init__(self):
        self.dtr = DataTableReader('matury.db', None)

    def arg_parser(self, arg_num, command):
        return str(sys.argv[arg_num]).lower() == command

    def set_sex(self):
        self.dtr.sex = self.arg_sex()

    def arg_sex(self):
        for iterator in range(1, len(sys.argv)):
            if self.arg_parser(iterator, "-k"):
                return True
            elif self.arg_parser(iterator, "-m"):
                return False
        return None

    def arg_checker(self, arg_num, check):
        if self.arg_parser(arg_num, check):
            return sys.argv[arg_num + 1]
        return None

#checks if 2 arguments of command line match to command regardless their sequence
    def arg_reader(self, actual, fun, check1, check2):
        actual += 1
        arg1 = cmd.arg_checker(actual, check1)
        if arg1 is not None:
            actual += 2
            arg2 = cmd.arg_checker(actual, check2)
            if arg2 is not None:
                if check1 == "region":
                    arg1 = arg1.lower().capitalize()
                if check2 == "region":
                    arg2 = arg2.lower().capitalize()
                fun(arg1, arg2)
            else:
                print('Poprawny argument "region", brak argumentu "rok"')
                return False
        return True

    def arg_numb_checker(self, actual, number, args):
        if len(sys.argv) < actual + number:
            print('Błędne arumenty, poprawne to ' + args)
            return False
        return True

    def run(self):
        for i in range(1, len(sys.argv)):
            if str(sys.argv[i]) == "-1":
                if not self.arg_numb_checker(i, 5, '"region" oraz "rok"'):
                    break
                if not cmd.arg_reader(i, self.dtr.avg_participants, "region", "rok"):
                    cmd.arg_reader(i, self.dtr.avg_participants, "rok", "region")
                break
            elif str(sys.argv[i]) == "-2":
                if not self.arg_numb_checker(i, 3, '"region"'):
                    break
                i += 1
                region = cmd.arg_checker(i, "region")
                if region is None:
                    print('Błędne arumenty, poprawne to "region"')
                    break
                region = region.lower().capitalize()
                self.dtr.percentage_passed(region)
                break
            elif str(sys.argv[i]) == "-3":
                if not self.arg_numb_checker(i, 3, '"rok"'):
                    break
                i += 1
                year = cmd.arg_checker(i, "rok")
                if year is None:
                    print('Błędne arumenty, poprawne to "rok"')
                    break
                self.dtr.best_region(year)
                break
            elif str(sys.argv[i]) == "-4":
                self.dtr.regression_checker()
            elif str(sys.argv[i]) == "-5":
                if not self.arg_numb_checker(i, 5, '"region" oraz "region"'):
                    break
                if not cmd.arg_reader(i, self.dtr.comparison, "region", "region"):
                    break

cmd = CmdInterface()
cmd.set_sex()
cmd.run()
