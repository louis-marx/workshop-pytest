from calculate.operators import Operators


def test_should_make_addition():
    sut = Operators()
    operation = "5.5 + 10"
    expected_value = 15.5
    assert sut.addition(operation) == expected_value
