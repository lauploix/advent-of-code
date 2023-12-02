import unittest

def solve_1 (lines):
    r = 0
    for line in lines:
        chars = [c for c in line if c >= "0" and c <= "9"]
        nbs = chars [0] + chars [-1]
        r = r + int (nbs)
    print (r)

class MyTests(unittest.TestCase):
    def test_examples(self):
        assert list(extract("one")) == ["1"]
        assert list(extract("onetwo")) == ["1", "2"]
        assert list(extract("twone")) == ["2", "1"]
        assert list(extract("two1nine")) == ["2", "1", "9"]
        assert list(extract("eightwothree")) == ["8", "2", "3"]
        assert list(extract("abcone2threexyz")) == ["1", "2", "3"]
        assert list(extract("xtwone3four")) == ["2", "1", "3", "4"]
        assert list(extract("4nineeightseven2")) == ["4", "9", "8", "7", "2"]
        assert list(extract("zoneight234")) == ["1", "8", "2", "3", "4"]
        assert list(extract("7pqrstsixteen")) == ["7", "6"]

    def test_digits(self):
        assert list(extract("onetwothreefourfivesixseveneightnine")) == ["1","2","3","4","5","6","7","8","9"]

    def test_example(self):
        s = """two1nine
                eightwothree
                abcone2threexyz
                xtwone3four
                4nineeightseven2
                zoneight234
                7pqrstsixteen"""
        assert solve_2(s.split()) == 281

    def test_example2(self):
        s = """1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet"""
        assert solve_2(s.split()) == 142


def extract(s):
    numbers= "one two three four five six seven eight nine".split(" ")
    extract_next = True
    if s:
        if s[0] >= "1" and s[0] <= "9":
            yield s[0]
        else:
            for i, item in enumerate(numbers):
                if s.startswith (item):
                    yield from extract (str(i+1) + s[1:])
                    return
        yield from extract (s[1:])

def solve_2 (lines):
    r = 0
    lines = list (lines)
    for line in lines:
        chars = [c for c in extract(line)]
        nb = chars [0] + chars [-1]
        r = r + int (nb)
    print (r)
    return r


if __name__=="__main__":
    import os
    d = os.path.split(__file__)[0]
    input_1 = os.path.join (d, "input.txt")
    input_2 = os.path.join (d, "input2.txt")
    if os.path.exists(input_2):
        with open (input_2) as f:
            solve_2(f)
    else:
        if os.path.exists(input_1):
            with open (input_1) as f:
                solve_1(f)
