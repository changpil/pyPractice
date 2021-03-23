"""
Problem Statement:
Given a point p, and other n points in two-dimensional space, find k points out of n points which are nearest to p.
NOTE: Distance between two points is measured by the standard Euclidean method.
Input/Output Format For The Function:
Input Format:
There are 4 arguments in input, an integer p_x, which is the x coordinate of point p, integer p_y, which is the y coordinate of point p, an integer k and a 2D integer array of points n_points.
Output Format:
Return a 2D integer array result, which contains k points, nearest to point p.
"""

import math
import collections
import heapq

def nearest_neighbours(p_x, p_y, k, n_points):
    heap = []
    for x, y in n_points:
        d = distance(p_x, p_y, x, y)
        if len(heap) == k and -heap[0][0] > d:
            heapq.heappop(heap)
            heapq.heappush(heap, (-d, (x, y)))
        elif len(heap) < k:
            heapq.heappush(heap, (-d, (x, y)))
        heapq.heappush(heap, (-d, (x, y)))
    queue = collections.deque()
    while heap:
        _, point = heapq.heappop(heap)
        queue.appendleft(point)
    return list(queue)


def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

points =[(0, 0), (1, 0)]
print(nearest_neighbours(1,1, 2, points))