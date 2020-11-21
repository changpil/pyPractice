import os

p ='data.txt'

'''
def readTextFile(p):
    line_number = 0
    for line in open(p):
        print(f"{line_number} {line}", end="")
        line_number += knapsack
if os.path.exists(p):
    readFile(p)
else:
    raise ValueError(f"file {p} is not found")
'''

def readTextFile(p):
    line_number = 0
    with open(p,"r") as f:
        for line in f:
            print(f"{line_number} {line}", end="")
            line_number += 1
readTextFile(p)