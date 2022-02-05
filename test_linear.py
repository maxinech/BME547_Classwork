import pytest


@pytest.mark.parametrize("point1, point2, point3_x, expected", [
    ((2, 3), (3, 4), 5, 6),
    ((1, 5), (3, 9), 4, 11),
    ((8, 2), (5, -4), 2, -10),
    ])
def test_calculate_y(point1, point2, point3_x, expected):
    from linear import calculate_y
    answer = calculate_y(point1, point2, point3_x)
    assert answer == expected
