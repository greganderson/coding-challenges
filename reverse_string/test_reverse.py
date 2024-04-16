from reverse import reverse


def test_reverse():
    a = "Hello"
    expected = "olleH"
    assert reverse(a) == expected
