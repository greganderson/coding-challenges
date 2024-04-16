from main import remove_middle


def test_remove_middle():
    assert remove_middle([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 5, 6, 7]
    assert remove_middle([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
