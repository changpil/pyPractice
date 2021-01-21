import math
from heapq import *



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance > other.distance


    def getPoint(self):
        return [self.x, self.y]

def kClosest(points, k: int):
    maxheap = []

    for point in points:
        newPoint = Point(point[0], point[1])

        if len(maxheap) < k:
            heappush(maxheap, newPoint)
        else:
            if newPoint.distance < maxheap[0].distance:
                p = heappop(maxheap)
                print(p.getPoint())
                heappush(maxheap, newPoint)
    returnA = []

    for p in maxheap:
        returnA.append(p.getPoint())
    return returnA

#print(kClosest([[1,3],[-2,2]], 1))
# print(kClosest([[1,3],[-2,2],[2,-2]], 2))

print(kClosest([[3,3],[5,-1],[-2,4]], 2))
