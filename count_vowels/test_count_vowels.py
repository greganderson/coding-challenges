from count_vowels import count_vowels


def test_count_vowels():
    a = "supercalifragilisticexpialidocious"
    expected = 16
    assert count_vowels(a) == expected
