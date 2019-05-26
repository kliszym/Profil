class Commands:

    @staticmethod
    def sex_checker(sex):
        if sex is None:
            return ""
        elif sex is True:
            return "AND Płeć = 'kobiety'"
        else:
            return "AND Płeć = 'mężczyźni'"

    @staticmethod
    def get_avg_participants(region, year, sex=None):
        return """
            SELECT Rok, AVG(suma) FROM
            (
                SELECT Rok, SUM(`Liczba osób`) AS suma FROM 
                (
                    SELECT Terytorium, Rok, `Liczba osób` FROM matury
                    WHERE Terytorium = '""" + region + """' """ + Commands.sex_checker(sex) + """
                )
                WHERE Rok BETWEEN 2010 AND """ + str(year) + """
                GROUP BY Rok
            )
            """

    @staticmethod
    def get_percentage_passed(region, sex=None):
        return """
            SELECT Rok, CAST(zdało AS FLOAT) / CAST(przystąpiło AS FLOAT) * 100 as `Procent zdawalności` FROM
            (
                SELECT Rok, SUM(`Liczba osób`) AS przystąpiło FROM matury
                WHERE Terytorium = '""" + region + """' AND `Przystąpiło/zdało` = 'przystąpiło' """ + Commands.sex_checker(sex) + """
                GROUP BY Rok
            ) AS table1 INNER JOIN 
            (
                SELECT Rok AS R, SUM(`Liczba osób`) AS zdało FROM matury
                WHERE Terytorium = '""" + region + """' AND `Przystąpiło/zdało` = 'zdało' """ + Commands.sex_checker(sex) + """
                GROUP BY Rok
            ) AS table2 ON table1.Rok = table2.R ORDER BY Rok
            """

    @staticmethod
    def get_regression(sex=None):
        return """
            SELECT Rok, Terytorium, CAST(zdało AS FLOAT) / CAST(przystąpiło AS FLOAT) * 100 as `Procent zdawalności` FROM
            (
                SELECT Rok, Terytorium, SUM(`Liczba osób`) AS przystąpiło FROM matury
                WHERE `Przystąpiło/zdało` = 'przystąpiło' """ + Commands.sex_checker(sex) + """
                GROUP BY Terytorium, Rok
            ) AS table1 INNER JOIN 
            (
                SELECT Rok AS R, Terytorium AS T, SUM(`Liczba osób`) AS zdało FROM matury
                WHERE `Przystąpiło/zdało` = 'zdało' """ + Commands.sex_checker(sex) + """
                GROUP BY Terytorium, Rok
            ) AS table2 ON table1.Terytorium = table2.T AND table1.Rok = table2.R  ORDER BY Terytorium, Rok
            """

    @staticmethod
    def get_best_region(year, sex=None):
        return """
            SELECT Terytorium, MAX(CAST(zdało AS FLOAT) / CAST(przystąpiło AS FLOAT) * 100) as `Procent zdawalności` FROM
            (
                SELECT Terytorium, SUM(`Liczba osób`) AS przystąpiło FROM matury
                WHERE Rok = """ + str(year) + """ AND `Przystąpiło/zdało` = 'przystąpiło' """ + Commands.sex_checker(sex) + """
                GROUP BY Terytorium
            ) AS table1 INNER JOIN 
            (
                SELECT Terytorium AS T, SUM(`Liczba osób`) AS zdało FROM matury
                WHERE Rok = """ + str(year) + """ AND `Przystąpiło/zdało` = 'zdało' """ + Commands.sex_checker(sex) + """
                GROUP BY Terytorium
            ) AS table2 ON table1.Terytorium = table2.T ORDER BY Terytorium
            """

    @staticmethod
    def get_comparison_base(region, sex=None):
        return """
        SELECT Rok, Terytorium, CAST(zdało AS FLOAT) / CAST(przystąpiło AS FLOAT) * 100 as `Procent zdawalności` FROM
        (
            SELECT Rok, Terytorium, SUM(`Liczba osób`) AS przystąpiło FROM matury
            WHERE Terytorium = '""" + region + """' AND `Przystąpiło/zdało` = 'przystąpiło' """ + Commands.sex_checker(sex) + """
            GROUP BY Terytorium, Rok
        ) AS table1 INNER JOIN 
        (
            SELECT Rok AS R, Terytorium AS T, SUM(`Liczba osób`) AS zdało FROM matury
            WHERE Terytorium = '""" + region + """' AND `Przystąpiło/zdało` = 'zdało' """ + Commands.sex_checker(sex) + """
            GROUP BY Rok
        ) AS table2 ON table1.Rok = table2.R ORDER BY Terytorium, Rok
        """

    @staticmethod
    def get_comparison(region1, region2, sex=None):
        return """
        SELECT main1.Rok, main1.Terytorium, main1.`Procent zdawalności`, main2.Terytorium, main2.`Procent zdawalności` FROM
        ( 
            """ + Commands.get_comparison_base(region1, sex) + """ 
        ) AS main1 INNER JOIN 
        ( 
            """ + Commands.get_comparison_base(region2, sex) + """
        ) AS main2 ON main1.Rok = main2.Rok
        """
