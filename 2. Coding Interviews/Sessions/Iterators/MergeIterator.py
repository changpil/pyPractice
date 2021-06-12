'''
MergedIterator()

Context:
int next()
boolean hasNext()

iter1 = iter([1,3,5])
iter2 = iter([2,4,6])

MergedIterator(iter1, iter2)
while(mergedIterator.hasNext()):
    mergedIterator.next()
[1,2,3,4,5,6]

'''

"""
    heapq.heappush(self.minheap, (v, listIter[i]))
TypeError: '<' not supported between instances of 'list_iterator' and 'list_iterator'

In order to use Heap, you need to to have __lt__() function. 
heapq.heappush(1, object())
heapq.heappush(1, object())

It will raise the same error
"""
# import heapq
# class MergedIterator:
#     def __init__(self, listIter):
#         self.minheap = []
#         for i in range(len(listIter)):
#             v = next(listIter[i], None)
#             if v:
#                 heapq.heappush(self.minheap, (v, listIter[i]))
#
#     def next(self):
#         if not self.minheap:
#             raise Exception
#
#         minV, minIter = heapq.heappop(self.minheap)
#         nextv = next(minIter, None)
#         if nextv:
#             heapq.heappush(self.minheap, (nextv, minIter))
#         return minV
#
#     def hasNext(self):
#         if not self.minheap:
#             return False
#         return True

import heapq
# class MergedIterator:
#     def __init__(self, listIter):
#         self.listIters = listIter
#         self.minheap = []
#         for i in range(len(listIter)):
#             v = next(listIter[i], None)
#             if v:
#                 heapq.heappush(self.minheap, (v, i))
#
#     def next(self):
#         if not self.minheap:
#             raise Exception
#
#         minV, i = heapq.heappop(self.minheap)
#         nextv = next(self.listIters[i], None)
#         if nextv:
#             heapq.heappush(self.minheap, (nextv, i))
#         return minV
#
#     def hasNext(self):
#         if not self.minheap:
#             return False
#         return True

import heapq
class MergedIterator:
    def __init__(self, listIter):
        self.minheap = []
        for i in range(len(listIter)):
            v = next(listIter[i], None)
            if v:
                heapq.heappush(self.minheap, (v, i, listIter[i]))

    def next(self):
        if not self.minheap:
            raise Exception

        minV, i, minIter = heapq.heappop(self.minheap)
        nextv = next(minIter, None)
        if nextv:
            heapq.heappush(self.minheap, (nextv, i, minIter))
        return minV

    def hasNext(self):
        if not self.minheap:
            return False
        return True

inputIterators = [
        iter([1, 3, 5]),
        iter([2, 4, 6]),
]
m = MergedIterator(inputIterators)
while m.hasNext():
    print(m.next())


print("#"*30)

inputIterators = [
    iter([1, 3, 5]),
    iter([2, 4, 6]),
    iter([1, 2, 6, 7, 9, 11])
]

m = MergedIterator(inputIterators)
while m.hasNext():
    print(m.next())