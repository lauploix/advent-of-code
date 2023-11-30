
def solve_1 (lines):
    for line in lines:
        print (line)

def solve_2 (lines):
    for line in lines:
        print (line)


if __name__=="__main__":
    import os
    d = os.path.split(__file__)[0]
    input_1 = os.path.join (d, "input_1.txt")
    input_2 = os.path.join (d, "input_2.txt")
    if os.path.exists(input_1):
        with open (input_1) as f:
            solve_1(f)
    if os.path.exists(input_2):
        with open (input_2) as f:
            solve_2(f)