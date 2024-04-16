from length_of_last_word import length_of_last_word

def test_get_length_of_last_word():
    assert length_of_last_word("All your base are belong to us") == 2
    assert length_of_last_word("She sells sea shells by the sea shore") == 5
    assert length_of_last_word("Coding is fun") == 3
