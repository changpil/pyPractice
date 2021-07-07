import math
def closestStraightCity(c, x, y, q):
    for i in range(len(c)):
        min_index = math.inf
        min_distance = math.inf
        for j in range(len(c)):
            if i == j:
                continue
            distance = abs(x[i] - x[j]) + abs(y[i] - y[j])
            if min_distance > distance:
                min_index = j
                min_distance = distance
            elif min_distance == distance:
                min_index == None
        if min_index == None:
            q.append(None)
        else:
            q.append(c[min_index])
    return q

c = ["c1", "c2", "c3"]
x = [2, 2, 4]
y = [1, 2, 3]
q = []

print(closestStraightCity(c, x, y, q))