def solve(lines):
    for l in lines:
        print (common(l))
    print (sum(prio(common(l)) for l in lines))

def solve2(lines):
    print ("lines: ", len(lines), " of them")
    total = 0
    for i in range(int(len(lines)/3)):
        l1 = lines[3*i]
        l2 = lines[3*i+1]
        l3 = lines[3*i+2]
        print ("line: ", 3*i, 3*i+1, 3*i+2)
        total = total + prio(commons(l1, l2, l3))
    print (total)

def commons(l1, l2, l3):
    s = set(l1).intersection(set(l2)).intersection(set(l3))
    assert len(s) == 1
    return s.pop()

def prio(letter):
    if ord(letter) <= ord ("Z"):
        return 27+ord(letter)-ord("A")
    return 1+ord(letter)-ord("a")

def common (line):
    l1 = line[:int(len(line)/2)]
    l2 = line[int(len(line)/2):]
    s1 = set(l1)
    s2 = set(l2)
    s = s1.intersection(s2)
    return s.pop()

if __name__=="__main__":
    assert (prio("a") == 1)
    assert (prio("A") == 27)
    assert (commons ("ab", "ac", "da") == "a")

    import os
    d = os.path.split(__file__)[0]
    input = os.path.join (d, "input.txt")
    with open(input, "r") as f:
        lines = f.read().splitlines()

    solve2(lines)