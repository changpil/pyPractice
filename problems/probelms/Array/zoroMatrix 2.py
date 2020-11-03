"""
if an element in an MxN matrix is 0,
its entire row and column are set to 0
"""
from pprint import pprint
def zero(wd):
    columnes=set()
    rows=set()
    i_c, i_r = 0, 0
    for row in wd:
        i_c = 0 # Missed this
        for col in row:
            if(col == '0'):
                columnes.add(i_c)
                rows.add(i_r)
            i_c += 1
        i_r += 1

    print("{} {}".format(columnes, rows))
    for j in columnes:
        for i in range(len(wd)):
            wd[i][j]='0'
    for i in rows:
        for j in range(len(wd[0])):
            wd[i][j]='0'


s=[list("123456") for _ in range(7) ]
s[6]=list("023450")
s[0]=list("123050")
pprint(s)
zero(s)
pprint(s)
