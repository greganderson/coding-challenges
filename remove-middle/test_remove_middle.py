from main import remove_middle


def test_remove_middle():
    start = [1, 2, 3, 4, 5, 6, 7]
    expected = [1, 2, 3, 5, 6, 7]
    result = remove_middle(start)
    assert result == 4
    assert start == expected

    even = [1, 2, 3, 4, 5, 6]
    expected = [1, 2, 3, 4, 5, 6]
    result = remove_middle(even)
    assert result is None
    assert even == expected

