import pytest

from ..main import func


@pytest.mark.parametrize('a, b, expected', [
    (1, 1, 2),
    (2, 3, 13),
])
def test_func(a, b, expected) -> None:
    assert func(a, b) == expected
