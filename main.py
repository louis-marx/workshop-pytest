# python -m doctest -v main.py


def to_absolute(number):
    """
    >>> to_absolute(-5)
    5
    >>> to_absolute(9)
    -9
    """
    if number <= 0:
        return -number
    return number
