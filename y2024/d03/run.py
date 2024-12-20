import unittest
import os
d = os.path.split(__file__)[0]
input_txt = os.path.join (d, "input.txt")
input_1 = os.path.join (d, "input1.txt")
input_2 = os.path.join (d, "input2.txt")




def solve_1 (f):
    import re
    

def solve_2 (f):
    pass

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



