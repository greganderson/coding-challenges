from palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("level") == True
    assert is_palindrome("dog") == False
    assert is_palindrome("madam") == True