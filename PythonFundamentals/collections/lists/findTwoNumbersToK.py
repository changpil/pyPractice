print("*"*10)
print("*  O(n^2) Brute Force *")
print("*"*10)
def find_sum(l,k):
    for i in range(len(l)):
        j = 0
        while j < i:
            if k == l[i] + l[j]:
                return [l[i], l[j]]
            j += 1

    return None
print(find_sum([3, 0, -5, 3, 9, 20, -20, 0], 0))
print(find_sum([5,5,5 ], 0))
print(find_sum([-5,-5,-5 ], -10))
print(find_sum([-1 ], 0))
print(find_sum([ ], 0))

print("*"*10)
print("*  O(nlogn) Binary BinarySearchVariants *")
print("*"*10)

def binary_search(l, k):
    i, j = 0 , len(l)-1
    while i <= j:
        mid = (i + j) // 2
        if k == l[mid]:
            return mid
        if l[mid] < k:
            i = mid + 1
        elif l[mid] > k:
            j = mid - 1
    return None

def find_sum(l,k):
    l.sort()
    for i in range(len(l)):
        j = binary_search(l, k - l[i])
        if j != None:
            return [l[i], l[j]]
    return None

print(find_sum([3, 0, -5, 3, 9, 20, -20, 0], 0))
print(find_sum([5,5,5 ], 0))
print(find_sum([-5,-5,-5 ], -10))
print(find_sum([-1 ], 0))
print(find_sum([ ], 0))

print("*"*10)
print("*  O(nlogn) Two moving indices *")
print("*"*10)

def find_sum(l,k):
    l.sort()
    i , j = 0, len(l)-1
    while i < j  :
        s = l[i] + l[j]
        if s == k:
            return [l[i], l[j]]
        elif s < k:
            i += 1
        else:
            j -= 1
    return None
print(find_sum([3, 0, -5, 3, 9, 20, -20, 0], 0))
print(find_sum([5,5,5 ], 0))
print(find_sum([-5,-5,-5 ], -10))
print(find_sum([-1 ], 0))
print(find_sum([ ], 0))