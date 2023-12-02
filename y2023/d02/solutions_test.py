import unittest

def solve_1 (lines):
    lines = list(lines)
    r = 0
    for i, game in enumerate(lines):
        possible = True
        draws = game.split(":")[1].split (";")
        for draw in draws:
            balls = [d.strip().split() for d in draw.split (",")]
            balls = [b[::-1] for b in balls]
            vals = dict(balls)
            if int(vals.get("red", "0")) > 12:
                possible = False
            if int(vals.get("green", "0")) > 13:
                possible = False
            if int(vals.get("blue", "0")) > 14:
                possible = False
        if possible:
            r += (i + 1)
    return r

def solve_2 (lines):
    r = 0
    lines = list(lines)
    for game in lines:
        nbs = {"red": 0, "blue": 0, "green": 0}
        draws = game.split(":")[1].split (";")
        for draw in draws:
            balls = [d.strip().split() for d in draw.split (",")]
            vals = dict([(b[1], int(b[0])) for b in balls])
            for k in nbs:
                nbs[k] = max (nbs[k], vals.get(k, 0))
        power = nbs["red"] * nbs["blue"] * nbs["green"] 
        r += power
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

def test_1():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    assert solve_1(s.split("\n")) == 8

def test_power():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    assert solve_2(s.split("\n")) == 2286
