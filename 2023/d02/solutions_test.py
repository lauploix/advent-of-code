import unittest

def solve_1 (lines):
    lines = list(lines)
    assert len(lines) == 100
    r = 0
    for i, game in enumerate(lines):
        print (i+1, game)
        possible = True
        draws = game.split(":")[1].split (";")
        for draw in draws:
            balls = [d.strip().split() for d in draw.split (",")]
            balls = [b[::-1] for b in balls]
            vals = dict(balls)
            print (vals)
            if int(vals.get("red", "0")) > 12:
                possible = False
            if int(vals.get("green", "0")) > 13:
                possible = False
            if int(vals.get("blue", "0")) > 14:
                possible = False
        if possible:
            r = r + i + 1
            print(r)
    print (r)
    return r

def solve_2 (lines):
    r = 0
    lines = list(lines)
    for game in lines:
        nbs = {"red": 0, "blue": 0, "green": 0}
        print (game)
        draws = game.split(":")[1].split (";")
        for draw in draws:
            balls = [d.strip().split() for d in draw.split (",")]
            vals = dict([(b[1], int(b[0])) for b in balls])
            for k in nbs:
                nbs[k] = max (nbs[k], vals.get(k, 0))
        power = nbs["red"] * nbs["blue"] * nbs["green"] 
        print(power)
        r += power
    return r

class MyTests(unittest.TestCase):
    def test_1(self):
        s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        assert solve_1(s.split("\n")) == 8

    def test_power(self):
        s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        assert solve_2(s.split("\n")) == 2286


if __name__=="__main__":
    import os
    d = os.path.split(__file__)[0]
    input_1 = os.path.join (d, "input1.txt")
    input_2 = os.path.join (d, "input2.txt")
    if os.path.exists(input_2):
        with open (input_2) as f:
            print (solve_2(f))
    else:
        if os.path.exists(input_1):
            with open (input_1) as f:
                print (solve_1(f))
