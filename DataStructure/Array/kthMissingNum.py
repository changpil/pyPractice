# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
'''
arr =[1,2,3,5] find kth missing number
index 0 1 2 3

     1 2 3 (4) 5 (6) (7) ...
     0 1 2     3
  k=        1     2   3

k = 1  return 4
k = 2  return 6
k = 3  return 7
...

arr=[9]  find kth missing number
k = 1
[9 (10)]

[9,    1000]
k = 1
return 10
arr=[1,   3,  7]
idx= 0    1   2
     0    1   3  :  3 = arr[i] - i - arr[0]

arr=[1, 400000, 100000000] k =400005
arr=[0    1       2      ]
     0

     cnt = num_of_missings_util_index(arr, i)
     if cnt < k:

     else:


def num_of_missings_util_index(arr, i):
     return arr[i] - i - arr[0]

'''


def num_of_missings_util_index(arr, i):
    return arr[i] - i - arr[0]


def kthMissingNum(arr, k):
    if arr == None:
        raise ValueError
    missingNum = 0
    for i in range(1, len(arr)):
        missingNum = num_of_missings_util_index(arr, i)
        if missingNum >= k:
            return arr[i - 1] + (k - num_of_missings_util_index(arr, i-1))

    return arr[-1] + (k - missingNum)

print(kthMissingNum([1, 3, 4, 5, 6, 7,  9], 2))
# O(N) n = size of arr
# O(log(N)
# arr =[1,2,3,5] find kth missing number
# 1 2 6  9
# 0 1 2  3
# 0 0 3  5
#           k = 4  return 7 =  6 + (4 - 3) = 6 + 1 = 7


# 1 3 4 5 6 7 8 9  k=1
#  0 1 2 3 4 5 6 7
#        ^
#  0 1 1 1 1 1 1 1

# O(logN)
def foo(arr, i, j, k):
    if i > j :
        return
    mid = (i + (j - i) // 2)
    missedNums = num_of_missings_util_index(arr, mid)

    if missedNums >= k:
        if mid -1 >= 0 and  num_of_missings_util_index(arr, mid-1) < k:
            return arr[mid - 1] + (k - num_of_missings_util_index(arr, mid-1))
        else:
            return foo(arr, i, mid -1, k)
    else:
        if mid == len(arr) -1:
            return arr[-1] + k - num_of_missings_util_index(arr, len(arr)-1)
        else:
            return foo(arr, mid +1, j, k)
print(foo([1, 3, 4, 5, 6, 7, 8, 9], 0, 8, 1))
print(foo([1, 3, 4, 5, 6, 7, 8, 9], 0, 8, 2))
print(foo([1, 3, 4, 5, 6, 9], 0, 6, 2))