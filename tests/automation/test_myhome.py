from stage import myhome


def test_lower_temperature():
    assert myhome.get_comfort(0) == "Il fait trop froid"


def test_higher_temperature():
    assert myhome.get_comfort(100) == "Il fait trop chaud"


def test_good_temperature():
    assert myhome.get_comfort(20) == "Tout va bien"


def test_lower_temperature_2():
    assert myhome.get_comfort_2(0) == "il ne fait pas bon"


def test_higher_temperature_2():
    assert myhome.get_comfort_2(100) == "il ne fait pas bon"


def test_good_temperature_2():
    assert myhome.get_comfort_2(20) == "il fait bon"
