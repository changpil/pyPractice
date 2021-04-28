# Generate Binary Numbers from 1 to n using a Queue
# n = 3
# result = ["1","10","11"]
# n = 5
# result = ["1","10","11", "100", "101"]
import collections

def find_bin(num):
    queue = collections.deque()
    queue.append("1")
    binaryNums = []
    for _ in range(num):
        lastBinary = queue.popleft()
        binaryNums.append(lastBinary)
        queue.append(lastBinary + "0")
        queue.append(lastBinary + "1")
    return binaryNums
print(find_bin(1))
print(find_bin(3))
print(find_bin(5))
print(find_bin(11))
print(find_bin(20))