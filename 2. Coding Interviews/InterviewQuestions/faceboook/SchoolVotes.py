# [-1, 0, 3]
# Candidates for 2
# output = 2

# arr[i] < 0, candidate 1
# 0<= arr[i] < n, vote goes for for same as arr[i]
# arr[i] >n, vote for candidate 2
# return votes for candidate 1


def foo(arr):
    h = {}
    n = len(arr)
    can1, can2 = 0,0
    for i in range(len(arr)):
        if arr[i] < 0:
            h[i] = 1
            can1 += 1
        elif 0 <= arr[i] < n:
            h[i] = -1
        else:
            h[i] = 2
            can2 += 1
    for i in range(len(arr)):
        if 0 <= arr[i] < n:
            re = checkVote(arr, h, i)
            if re == 1:
                can1 += 1
            elif re == 2:
                can2 += 1
    return can1

def checkVote(arr, h, i):
    if arr[i] == i:
        return -1
    if h[i] != -1:
        return h[i]
    return checkVote(arr, h, arr[i])
v=  [1, -1, 0]

print(foo(v))
v=  [0, 0, 1]

print(foo(v))
