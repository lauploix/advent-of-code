import unittest
import os
d = os.path.split(__file__)[0]
input_txt = os.path.join (d, "input.txt")
input_1 = os.path.join (d, "input1.txt")
input_2 = os.path.join (d, "input2.txt")


def is_safe (data):
    pairs = [data[i:i+2] for i in range (len(data)-1)]
    abss = [abs(a-b) for (a, b) in pairs]
    signs = [(a>b) for (a, b) in pairs]
    monotone = len(set(signs)) == 1
    diffs = all ((d > 0 and d < 4) for d in abss)
    if monotone and diffs : 
        return True
    return False


def solve_1 (f):
    safes = 0
    for l in f:
        data = [int(a) for a in l.split()]
        if is_safe(data): 
            safes += 1
    return safes

def solve_2 (f):
    safes = 0
    for l in f:
        data = [int(a) for a in l.split()]
        if is_safe(data): 
            safes += 1
        else:
            for i in range (len(data)):
                dat = data.copy()
                del dat[i]
                if is_safe(dat):
                    safes += 1
                    break
    return safes

if __name__=="__main__":
    if os.path.exists(input_txt): #If thsi is the same input for both
        with open (input_txt) as f:
            print (solve_1(f))
        with open (input_txt) as f:
            print (solve_2(f))
    elif os.path.exists(input_1): #If there we have 2 input files
        with open (input_1) as f:
            print (solve_1(f))
        if os.path.exists(input_2):
            with open (input_2) as f:
                print (solve_2(f))
    else:
        print ('No input Ffle')

# ------------



