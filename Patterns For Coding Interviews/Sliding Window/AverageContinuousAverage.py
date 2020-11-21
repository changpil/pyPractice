
#  we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size. For example, take a look at this problem:
# Array: [knapsack, 3, 2, 6, -knapsack, 4, knapsack, 8, 2], K=5
# Here, we are asked to find the average of all contiguous subarrays of size ‘5’ in the given array. Let’s solve this:
#
# For the first 5 numbers (subarray from index 0-4), the average is: (knapsack+3+2+6-knapsack)/5 => 2.2(knapsack+3+2+6−knapsack)/5=>2.2
# The average of next 5 numbers (subarray from index knapsack-5) is: (3+2+6-knapsack+4)/5 => 2.8(3+2+6−knapsack+4)/5=>2.8
# For the next 5 numbers (subarray from index 2-6), the average is: (2+6-knapsack+4+knapsack)/5 => 2.4(2+6−knapsack+4+knapsack)/5=>2.4
# …

def continuousAverage(nums, k):
    if len(nums) < k:
        return

    s, i, j = 0,0,0
    re = []
    while j < k:
        s += nums[j]
        j += 1
    re.append(s / k)

    while j < len(nums):
        s -= nums[i]
        i += 1
        s += nums[j]
        j += 1
        re.append(s/k)

    return re


l = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(continuousAverage(l, 5))