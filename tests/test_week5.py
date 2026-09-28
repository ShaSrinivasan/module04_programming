import math


def test_tax_at_seven_percent():
    subtotal = 200.00
    tax = subtotal * 0.07
    assert math.isclose(tax, 14.0)


def test_over_limit_true():
    value = 1500
    limit = 1000
    assert value > limit


def test_over_limit_false():
    value = 500
    limit = 1000
    assert not (value > limit)


def test_type_of_string():
    name = "ISM3232"
    assert type(name) == str


def test_type_conversion():
    s = "42"
    assert int(s) == 42
