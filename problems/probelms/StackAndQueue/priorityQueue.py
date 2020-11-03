"""
implement a priority queue using queues
"""
# class PriorityQueue:
#     def __init__(self,size=None):
#         self.q1 = list()
#         self.size = size
#
#     def push(self, i):
#         self.q1.append(i)
#
#     #O(n)
#     def pop(self):
#         if len(self.q1) <= 0 :
#             raise IndexError
#         min_v, min_p = list[0], 0
#         for v, i in enumerate(self.q1):
#             if v < min_v:
#                 min_v, min_p = v, i
#         del self.q1[min_p]
#         return min_v
#
#     #O(n)
#     def peak(self):
#         if len(self.q1) <= 0 :
#             raise IndexError
#         min_v, min_p = list[0], 0
#         for v, i in enumerate(self.q1):
#             if v < min_v:
#                 min_v, min_p = v, i
#         return min_v
#
#     def isEmpty(self):
#         return bool (len(self.q1))
#
#     def size(self):
#         return self.size

#######################################################
"""
Generic implementation of a priority queue using queues
"""
class PriorityQueue:
    def __init__(self,size=None, reversed = False):
        self.qs = list()
        self.items = list()
        self.size = size
        self.reversed= -1 if reversed == True else 1

    def put(self, priority, item):
        if self.size <= len(self.qs):
            raise IndexError
        self.qs.append(self.reversed*priority)
        self.items.append(item)

    #O(n)
    def get(self):
        if len(self.qs) <= 0 :
            raise IndexError
        min_v, min_p = self.qs[0], 0
        for i, v in enumerate(self.qs):
            if v < min_v:
                min_v, min_p = v, i
        min_v = self.items[min_p]
        del self.qs[min_p]
        del self.items[min_p]
        return min_v

    #O(n)
    def peak(self):
        if len(self.q1) <= 0 :
            raise IndexError
        min_v, min_p = list[0], 0
        for v, i in enumerate(self.q1):
            if v < min_v:
                min_v, min_p = v, i
        return self.items[min_p]

    def isEmpty(self):
        return bool (len(self.qs))

    def size(self):
        return self.size

q =PriorityQueue(3, reversed=True)
q.put(6,[6,7,8])
q.put(0,[0,1,2])
q.put(3,[3,4,5])

print(q.get())