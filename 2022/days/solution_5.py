def solve(lines):
    for l in lines: print (repr(l))

if __name__=="__main__":

    import os
    d = os.path.split(__file__)[0]
    input = os.path.join (d, "/Users/plume/Documents/GitHub/advent-of-code/2022/days/adventofcode.com_2022_day_5_input.txt")
    with open(input, "r") as f:
        lines = f.read().splitlines()

    solve(lines)    
  