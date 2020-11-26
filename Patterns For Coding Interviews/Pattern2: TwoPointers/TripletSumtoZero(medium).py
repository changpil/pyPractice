# Problem Statement #
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
#
# Example 1:
#
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:
#
# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.


# OPtion1L three loops O(N^3)
# After Sort - three pointers O(NlogN)
# MaxHeap and MinHeap and binarySearch : O(NlogN) Sorted for binarySearch: extra space(N)

# using Dictionary O(N^2)
# This is not correct implemtation
def search_triplets(arr):
  triplets = []
  twoSums = dict()
  for i in range(0, len(arr)):
    for j in range(i +1, len(arr)):
      if arr[i] + arr[j] not in twoSums:
        twoSums[arr[i]+ arr[j]] = [[arr[i], arr[j]]]
      else:
        twoSums[arr[i] + arr[j]].append( [arr[i], arr[j]] )
  print(twoSums)

  for i  in  range(len(arr)):
    t = arr[i] * -1
    if t in twoSums:
      for a in twoSums[t]:
        triplets.append( list(a) + [arr[i]] )

  t = map(lambda x: tuple(sorted(x)), triplets)

  return list(set(t))
print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))

def search_triplets(arr):
  triplets = []
  twoSums = dict()
  for i in range(0, len(arr)):
    for j in range(i +1, len(arr)):
      if arr[i] + arr[j] not in twoSums:
        twoSums[arr[i]+ arr[j]] = [[i, j]]
      else:
        twoSums[arr[i] + arr[j]].append([i,j])
  tmp =[]
  for i  in  range(len(arr)):
    t = arr[i] * -1
    if t in twoSums:
      for a in twoSums[t]:
        tmp.append(a + [i])
  print(tmp)

  # Remove duplicated indices
  tup = map(lambda x: tuple(sorted(x)), tmp)
  tup = filter(lambda x: x[0]!= x[1] and x[1] != x[2] ,tup)
  s = set(tup)
  #print(s)
  tmp.clear()
  for l in s:
    re = []
    for index in l:
      re.append(arr[index])
    tmp.append(re)

  # remove ducplcated element [2,1,1] [1,2,1] from different index has the same values
  tup = map(lambda x: tuple(sorted(x)), tmp)
  tup = list(set(tup))
  triplets = map(lambda x: list(sorted(x)), tup)
  return list(triplets)


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))

print("#"*100)
# Educative Solution

# O(n^2)
def triplets(arr):
    arr.sort()
    i, l, r = 0, 0, 0
    re = []

    while arr[i] <= 0:
        l = i + 1
        r = len(arr) -1
        target = -1 * arr[i]

        while l < r:
            if arr[l] + arr[r] > target :
                r -= 1
            elif arr[l] + arr[r] < target:
                l += 1
            else:
                re.append([arr[i], arr[l], arr[r]])
                while l < r and arr[l] == arr[l+1]:
                    l += 1
                while l < r and arr[r] == arr[r-1]:
                    r -= r
                l += 1
                r -= 1
        i += 1
    return re

print(triplets([-3, 0, 1, 2, -1, 1, -2]))
print(triplets([-5, 2, -1, -2, 3]))