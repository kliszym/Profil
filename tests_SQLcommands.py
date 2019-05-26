from SQLcommands import Commands


def test_sex_checker():
    sex = None
    assert Commands.sex_checker(sex) == ""
    sex = True
    assert Commands.sex_checker(sex) == "AND Płeć = 'kobiety'"
    sex = False
    assert Commands.sex_checker(sex) == "AND Płeć = 'mężczyźni'"


def test_get_avg_participants():
    region = 'Polska'
    year = 2011
    test_string = Commands.get_avg_participants(region, year)
    assert "Terytorium = 'Polska'" in test_string
    assert "Rok BETWEEN 2010 AND 2011" in test_string
    assert "Płeć = 'kobiety"'' not in test_string
    assert "Płeć = 'mężczyźni" not in test_string


def test_get_percentage_passed():
    region = 'Mazowieckie'
    test_string = Commands.get_percentage_passed(region, True)
    assert "Terytorium = 'Mazowieckie'" in test_string
    assert "AND Płeć = 'kobiety'" in test_string


def test_get_regression():
    assert "AND Płeć = 'mężczyźni'" in Commands.get_regression(False)


def test_get_best_region():
    year = 2011
    test_string = Commands.get_best_region(year)
    assert "Rok = 2011" in test_string
    assert "Płeć" not in test_string


def test_comparison_base():
    region = "Dolnośląskie"
    test_string = Commands.get_comparison_base(region, True)
    assert "Terytorium = 'Dolnośląskie'" in test_string
    assert "AND Płeć = 'kobiety'" in test_string


def test_comparison():
    region1 = "Małopolskie"
    region2 = "Lubelskie"
    test_string = Commands.get_comparison(region1, region2, False)
    assert "Terytorium = 'Małopolskie'" in test_string
    assert "Terytorium = 'Lubelskie'" in test_string
    assert "AND Płeć = 'mężczyźni'" in test_string
