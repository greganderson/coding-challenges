import pytest

import even_numbers

def test_even_numbers():
    numbers = [1,2,3,4,5,6,7,8]
    total = 20
    assert even_numbers.sum_even_numbers(numbers) == total
