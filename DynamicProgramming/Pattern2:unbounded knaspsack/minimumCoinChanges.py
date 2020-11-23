# Introduction #
# Given an infinite supply of ‘n’ coin denominations and a t money amount, we are asked to find the minimum number of coins needed to make up that amount.
#
# Example 1:
#
# Denominations: {1,2,3}
# Total amount: 5
# Output: 2
# Explanation: We need minimum of two coins {2,3} to make a total of '5'
# Example 2:
#
# Denominations: {1,2,3}
# Total amount: 11
# Output: 4
# Explanation: We need minimum four coins {2,3,3,3} to make a total of '11'


import math


def count_change(d, t):
  result = _minimumCoins(d, t, 0)
  return -1 if result == math.inf else result


def _minimumCoins(d, t, i):
  # base check
  if t == 0:
    return 0

  n = len(d)
  if n == 0 or i >= n:
    return math.inf

  # recursive call after selecting the coin at the i
  # if the coin at i exceeds the t, we shouldn't process this
  count1 = math.inf
  if d[i] <= t:
    count1 = 1 + _minimumCoins(d, t - d[i], i)
  count2 = _minimumCoins(d, t, i + 1)

  return min(count1, count2)



print(count_change([1, 2, 3], 5))
print(count_change([1, 2, 3], 11))
print(count_change([1, 2, 3], 7))
print(count_change([3, 5], 7))