"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.
For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.
"""

import heapq
import math


# Timeout
# def maxFromThreeValues(A):
#     maxheap = []
#     minheap = []
#
#     for i in range(len(A)):
#         for j in range(i + 1, len(A)):
#             p = A[i] * A[j]
#             if len(minheap) == 0 or len(maxheap) == 0:
#                 heapq.heappush(minheap, (p, {i, j}))
#                 heapq.heappush(maxheap, (-p, {i, j}))
#             else:
#                 heapq.heappushpop(minheap, (p, {i, j}))
#                 heapq.heappushpop(maxheap, (-p, {i, j}))
#     maxV = -math.inf
#     for i in range(len(A)):
#         if A[i] < 0:
#             if minheap[0][0]*A[i] > maxV and i not in minheap[0][1]:
#                 maxV = minheap[0][0]*A[i]
#         else:
#             if maxheap[0][0]*A[i]*-1 > maxV and i not in maxheap[0][1]:
#                 maxV = -1*maxheap[0][0]*A[i]
#
#     return maxV

# 0(NlogN)
def maxFromThreeValues(A):
    A.sort()
    for i in range(2, len(A)):
        if A[i] < A[i-1] + A[i-2]:
            return 1
    return 0
A = [-3, 1, 2, -2, 5, 6]
print(maxFromThreeValues(A))