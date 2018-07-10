import pytest

from nth_fib import n_fib

test_cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144),
    (13, 233),
]


@pytest.mark.parametrize("a, expected", test_cases)
def test_fib(a, expected):
    assert n_fib(a) == expected
