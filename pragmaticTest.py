def test_passing1():
    assert (1, 2, 3) == (1, 2, 3)


def test_passing2():
    assert (1, 2, 3) == (1, 2, 33)


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('bicycle') == 'Bicycle'
