import convert


def test_convert():
    a = "ABE"
    expected = ["483"]
    assert convert.convert(a) == expected
