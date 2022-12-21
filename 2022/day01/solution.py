def solve(input):
    with open(input, "r") as f:
        lines = f.read().splitlines()
    
    l = [sum(g) for g in y_groups(lines)]
    l.sort()
    print (l[-3:], sum(l[-3:]))
        

def y_groups (l):
    g = []
    for item in l:
        if item == "":
            yield g
            g = []
        else:
            g.append(int(item))
    yield g

if __name__=="__main__":
    import os
    d = os.path.split(__file__)[0]
    input = os.path.join (d, "input.txt")
    solve(input)