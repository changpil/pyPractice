"""
if an element in an MxN matrix is 0,
its entire row and column are set to 0
"""

def zeroMatrix(m):
    l=[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                l.append((i,j))

    if len(l) == 0:
        return m

    r_l = [i[0] for i in l]
    c_l= [i[1] for i in l]

    for i in range(len(m)):
        for j in range(len(m[0])):
            if r_l.count(j) !=0 or c_l.count(i) != 0:
                m[i][j] =0

    return m

m = [[i for i in range(1,10)] for j in range(5)]

m[2][3] = 0
import pprint
pprint.pprint(zeroMatrix(m))