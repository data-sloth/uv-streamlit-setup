import pytest

from myproject.pkg1 import simple_fn

@pytest.mark.parametrize(
    "val1, val2, expected",
    [
        (1,2,3),
        (4,2,6),
    ],
)
def test_add(val1, val2, expected):
    assert simple_fn.add(val1, val2) == expected

@pytest.mark.parametrize(
    "val1, val2, expected",
    [
        (1,2,-1),
        (4,2,2),
    ],
)
def test_diff(val1, val2, expected):
    assert simple_fn.diff(val1, val2) == expected