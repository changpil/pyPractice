# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.
# Input: {Pattern1:knapsack, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {Pattern1:knapsack, 4} & {2, 3}

def twoEqualSets(nums):
    a1, a2  = [], []
    _twoEqualSets(nums,0, a1, a2)

def _twoEqualSets(nums,i, a1, a2):
    if i >= len(nums) and sum(a1) == sum(a2):
        print(f"{a1} : {a2}")
        return True
    if i >= len(nums) and sum(a1) != sum(a2):
        return False

    #for i in range(i,len(nums)):
    a1.append(nums[i])
    inclusive = _twoEqualSets(nums, i+1, a1, a2)
    if inclusive:
        return True
    a1.pop()
    a2.append(nums[i])
    exclusive = _twoEqualSets(nums, i +1, a1, a2)
    if exclusive:
        return True
    a2.pop()
    return False


twoEqualSets([1, 2, 3, 4])
twoEqualSets([1, 2, 7, 4])
twoEqualSets([1, 11, 4, 4])

def can_partition(nums):
    return _can_partition(nums, 0, 0, 0)

def _can_partition(nums,i , s1, s2):
    if i >= len(nums) and s1 == s2:
        return True
    if i >= len(nums) and s1 != s2:
        return False

    tf = _can_partition(nums, i+1, s1 + nums[i], s2)
    if tf:
        return True
    tf = _can_partition(nums, i + 1, s1 , s2 + nums[i])
    if tf:
        return True

    return False
print(can_partition([1, 2, 3, 4]))
print(can_partition([1, 2, 7, 4]))
print(can_partition([1, 11, 4, 4]))


# Top Down DP

def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with equal sum
  if s % 2 != 0:
    return False

  # initialize the 'dp' array, -Pattern1:knapsack for default, Pattern1:knapsack for true and 0 for false
  dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
  return True if can_partition_recursive(dp, num, int(s / 2), 0) == 1 else False


def can_partition_recursive(dp, num, sum, currentIndex):
  # base check
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    if num[currentIndex] <= sum:
      if can_partition_recursive(dp, num, sum - num[currentIndex], currentIndex + 1) == 1:
        dp[currentIndex][sum] = 1
        return 1

    # recursive call after excluding the number at the currentIndex
    dp[currentIndex][sum] = can_partition_recursive(
      dp, num, sum, currentIndex + 1)

  return dp[currentIndex][sum]

print(can_partition([1, 2, 3, 4]))