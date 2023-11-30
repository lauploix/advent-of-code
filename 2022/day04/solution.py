def solve(lines):
    s = 0
    for l in lines:
        if ((l[0][0] <= l[1][0]) and (l[0][1] >= l[1][1])) :
            s = s + 1
        elif ((l[0][0] >= l[1][0]) and (l[0][1] <= l[1][1])) :
            s = s + 1
    print (s)

def solve2(lines):
    s = 0
    for l in lines:
        if ((l[0][0] <= l[1][1]) and (l[0][1] >= l[1][0])) :
            s = s + 1
    print (s)

def parse(lines):
    for line in lines:
        l = line.split(",")
        ints = [l1.split("-") for l1 in l]
        ints[0][0] = int(ints[0][0])
        ints[1][0] = int(ints[1][0])
        ints[0][1] = int(ints[0][1])
        ints[1][1] = int(ints[1][1])
        yield ints

if __name__=="__main__":

    import os
    d = os.path.split(__file__)[0]
    input = os.path.join (d, "input.txt")
    with open(input, "r") as f:
        lines = f.read().splitlines()

    solve(parse(lines))    
    solve2(parse(lines))