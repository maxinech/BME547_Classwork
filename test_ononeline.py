import pytest


@pytest.mark.parametrize("point1, point2, point3, expected", [
    ((2, 3), (3, 4), (5, 6), True),
    ((1, 5), (3, 9), (4, 11), True),
    ((8, 2), (5, -6), (2, -10), False),
    ((0, 7), (1, -1), (-3, 30), False),
    ])
def test_ononeline(point1, point2, point3, expected):
    from ononeline import judge_ononeline
    answer = judge_ononeline(point1, point2, point3)
    assert answer == expected
