# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.


# Follow up:
# Could you do get and put in O(1) time complexity?

# O(n)
# Heapq with (datetime.now().timestamp(), key) did not solve the problem.
# Needed to heapify again after delete key in [].
# You do not need heapify with heappop and heappush. But you need to heapify after del self.heap.remove(key)
from heapq import *
from datetime import datetime

class Item:
    def __init__(self, ts, key):
        self.ts = ts
        self.key = key
    def __lt__(self, o):
        return self.ts < o.ts
        #return o.ts - self.ts
    def __str__(self):
        return f"[{self.ts}: {self.key}]"

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.heap = []

    def removeHeap(self, key):
        for i in range(len(self.heap)):
            if self.heap[i].key == key:
                #print(self.heap[i])
                del self.heap[i]
                heapify(self.heap)
                break

    def get(self, key: int) -> int:
        #print(f"get {key} ")
        if key not in self.cache:
            return -1

        self.removeHeap(key)
        heappush(self.heap, Item(datetime.now().timestamp(), key))
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        #print(f"put {key} ")
        if key in self.cache:
            self.removeHeap(key)
            self.cache.pop(key)

        if len(self.cache) == self.capacity:
            evict = heappop(self.heap)
            self.cache.pop(evict.key)

        heappush(self.heap, Item(datetime.now().timestamp(), key))
        self.cache[key] = value
        #print(self.cache)

# O(n)
class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node()
        self.tail = self.head
        self.cache = {}

    def put(self, key, val):
        # Cache capacity is full, remove RLU cache
        if self.capacity == len(self.cache):
            # remove tail of node
            removalKey = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            self.cache.pop(removalKey)

        newNode = Node(val, None, None)
        sentinel = self.head
        next = sentinel.next
        sentinel.next = newNode
        newNode.prev = sentinel
        newNode.prev = next
        if next:
            next.prev = newNode
        if self.tail == sentinel:
            self.tail = newNode

        self.cache[key] = newNode

    def get(self, key):
        if key not in self.cache:
            raise ValueError()

        node = self.cache[key]
        returnValue = node.val
        prev, next = node.prev, node.next
        prev.next = next
        if next:
            next.prev = prev
        else:
            self.tail = prev
        self.cache.pop(key)
        self.put(key, returnValue)

        return returnValue

lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    #return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1) # cache is {1=1}
# lRUCache.put(2, 2) # cache is {1=1, 2=2}
# print(lRUCache.get(1))    # return 1
# lRUCache.put(1, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(1))    # returns -1 (not found)
