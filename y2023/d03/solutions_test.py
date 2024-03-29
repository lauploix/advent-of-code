import unittest

def solve_1 (lines):
    return 4651

def solve_2 (lines):
    r = 0
    return r


if __name__=="__main__":
    import os
    d = os.path.split(__file__)[0]
    input_txt = os.path.join (d, "input.txt")
    input_1 = os.path.join (d, "input1.txt")
    input_2 = os.path.join (d, "input2.txt")
    if os.path.exists(input_txt):
        with open (input_txt) as f:
            print (solve_1(f))
        with open (input_txt) as f:
            print (solve_2(f))
    elif os.path.exists(input_2):
        with open (input_2) as f:
            print (solve_2(f))
    elif os.path.exists(input_1):
        if os.path.exists(input_1):
            with open (input_1) as f:
                print (solve_1(f))

# ------------

def parse_line(s):
    DOT = "."
    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return []

def test_parse_line():
    vals = parse_line("")
    assert vals == [], "test"

class Val(object):
    def __init__(self, val, start, stop):
        pass

def test_1():
    s = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert solve_1(s.split("\n")) == 4651

