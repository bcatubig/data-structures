import quicksort
import pytest

testdata = [
    (
        [11, 900, 888, 23, 54, 2192, 3, 89, 75, 64, 45],
        [3, 11, 23, 45, 54, 64, 75, 89, 888, 900, 2192],
    ),
    ([10, 1, 5, 99, 2, 33, 4], [1, 2, 4, 5, 10, 33, 99]),
    ([-99, 100, 5, 1, -4, 98, 30], [-99, -4, 1, 5, 30, 98, 100]),
]


@pytest.mark.parametrize("a,expected", testdata)
def test_quicksort(a, expected):
    result = quicksort.quicksort(a)

    assert result == expected
