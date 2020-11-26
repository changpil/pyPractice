# Quadruple Sum to Target (medium) #
# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
#
# Example 1:
#
# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.
# Example 2:
#
# Input: [2, 0, -1, 1, -2, 2], target=2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.
#

# O(N^3)

def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    i1, i2, j1,j2 = 0,0,0,0

    while i1 <len(arr)-4:
        j1 = len(arr) - 1
        while j1 > i1 + 2:
            t = target - (arr[i1] + arr[j1])
            i2, j2 = i1 +1 , j1 -1

            while i2 < j2:
                if arr[i2] + arr[j2] == t:
                    quadruplets.append([arr[i1], arr[i2], arr[j1], arr[j2]])
                    break
                elif arr[i2] + arr[j2] < t:
                    i2 +=  1
                else:
                    j2 -= 1
            j1 -=1
            # I did not handle this duplicated case
            while j1 > i1 and arr[j1] == arr[j1+1]:
                j1 -= 1
        i1 += 1
        # I did not handle this duplicate cases
        while i1 < j1 and arr[i1] == arr[i1-1]:
            i1 += 1
    return quadruplets

#print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))
print(search_quadruplets([2, -1,-1, -1, 0, 0,0,0,1,1,1,1,1], 0))