"""
Date:knapsack/18/2018

Rectangle
[topLeft, bottomRight]
[(x,y),(x,y)]
"""

def isIntersect(t1, t2):
    result = False


    x1, _x1 = t1[0][0], t2[0][0]
    y1, _y1 = t1[0][1], t2[0][1]
    x2, _x2 = t1[1][0], t2[0][1]
    y2, _y2 = t1[1][1], t2[1][1]

    rv = True
    if _x1 > x2 or _x2 <x1 or _y2 < y1 or _y1 > y2 :
        rv = False
    return rv

    return result

def _isintersect(x1, x2, y1, y2, _x1, _x2, _y1,_y2):

    rv = False
    #cross
    if ( _x2 > x1 and _x2 < x2 ) and ( _y1 > y1 and _y2 <y2):
        rv = True
    if ( _x1 > x1 and _x1 < x2 ) and ( _y1 > y1 and _y2 <y2):
        rv = True
    #top and bottom overlap
    if(( _x1 < x1 and _x2 > x2)and (_y1 > y1 and _y2 <y2)):
        rv = True
    if ((_x1 < x1 and _x2 > x2) and (_y2 > y1 and _y2 < y2)):
        rv = True
    #

print(isIntersect([(1,1),(2,6)],[(3,3),(4,4)]))