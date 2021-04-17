"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.
"""

### TimeOver O(N*M)
def solution1(N, A):
    maxCounter = 0
    result = [0]* N
    for i in range(len(A)):
        if A[i] == N + 1:
            for k in range(len(result)):
                result[k] = maxCounter
        else:
            result[A[i]-1] += 1
            maxCounter = max(maxCounter, result[A[i]-1])
        # print(result)
    return result


def solution2(N, A):
    lastN_1 = -1
    for i in range(len(A)):
        if A[i] == N + 1:
            lastN_1 = i
    maxCounters = [0] * N
    if lastN_1 != -1:
        duplicates = [0] * N
        max_dup = -1
        for i in range(0, lastN_1):
            if A[i] != N + 1:
                duplicates[A[i] - 1] += 1
                max_dup = max(max_dup, duplicates[A[i] - 1])
        maxCounters = [max_dup] * N

    for i in range(lastN_1+1, len(A)):
        maxCounters[A[i]-1] += 1
    return maxCounters

# A = [3,4,4,6,1,4,4]
# print(solution(5, A))  # [3, 2, 2, 4, 2]

# A = [3,4,4,2,1,4,4, 5]
# print(solution(5, A)) # [1, 1, 1, 4, 1]

# A = [3]
# print(solution(5, A)) # [0, 0, 1, 0, 0]


# A = [3,4,4,2,6,4,4, 5, 6, 3, 4, 1, 6]
# print(solution(5, A))


# A = [1,1,2,6,1,1,1,6,1]
# print(solution1(5, A))
# print(solution2(5, A))
#
#
#
# A = [6,6,6,6,1,6,6,6,6, 6]
# print(solution1(5, A))
# print(solution2(5, A))
#
#
# A = [0,0,1, 3,7,  2,7, 3,4,5,6,6,6,6,4, 4, 6, 7, 1,6,6,6,6,1,2,3,4,5, 7, 1,  6, 8]
# print(solution1(8, A))
# print(solution2(8, A))


def solution(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            dst_i = nums[i] - 1
            if  not (0 <= dst_i < len(nums)) or nums[dst_i] == dst_i + 1:
                break
            else:
                nums[dst_i], nums[i] = nums[i] , nums[dst_i]

    for i in  range(len(nums)):
        if nums[i] != i +1:
            return i + 1
    return len(nums) + 1

nums =  [-1, -3]

print(solution(nums))