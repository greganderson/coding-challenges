from age import age_in_days

def test_age():
    age = 20
    expected = 7300
    assert age_in_days(age) == expected