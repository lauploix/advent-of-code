def solve(input):
    with open(input, "r") as f:
        lines = f.read().splitlines()
    print (lines)
    print (sum([score2(l) for l in lines]))

def win(ax):
    if (ax) in ("A Y", "B Z", "C X"): return 6
    if (ax) in ("A X", "B Y", "C Z"): return 3
    return 0

def card (ax):
    xyz = ax[2]
    if xyz == "X": return 1
    if xyz == "Y": return 2
    return 3

def score (ax):
    return win(ax) + card (ax)
            
def score2 (ax):
    if ax[0] == "A":
        if ax [2] == "X": return score ("A Z")
        if ax [2] == "Y": return score ("A X")
        return score ("A Y")
    if ax[0] == "B":
        if ax [2] == "X": return score ("B X")
        if ax [2] == "Y": return score ("B Y")
        return score ("B Z")
    if ax[0] == "C":
        if ax [2] == "X": return score ("C Y")
        if ax [2] == "Y": return score ("C Z")
        return score ("C X")
            
if __name__=="__main__":
    assert (score2 ("A Y") == 4, score2 ("A Y"))
    assert score2 ("B X") == 1
    assert score2 ("C Z") == 7

    import os
    d = os.path.split(__file__)[0]
    input = os.path.join (d, "input.txt")
    solve(input)