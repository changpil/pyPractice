# Problem Statement #
# Given a number array representing the wealth of ‘n’ houses, determine the maximum amount of money the thief can steal without alerting the security system.
#
# Example 1:
#
# Input: {2, 5, 1, 3, 6, 2, 4}
# Output: 15
# Explanation: The thief should steal from houses 5 + 6 + 4
# Example 2:
#
# Input: {2, 10, 14, 8, 1}
# Output: 18
# Explanation: The thief should steal from houses 10 + 8
import math

def houseThief(wealth,n , included = False):
    if n < 0:
        return 0
    _max = -math.inf
    if included == False:
        m1 = houseThief(wealth, n-1, False)
        m2 = wealth[n] + houseThief(wealth, n-1, True)
        _max = max(m1, m2)
    else:
        _max = houseThief(wealth, n-1, False)
    return _max

l = [2, 5, 1, 3, 6, 2, 4]
print(houseThief(l ,len(l) - 1) )

l = [2, 10, 14, 8, 1]
print(houseThief(l ,len(l) - 1) )



def find_max_steal(wealth):
  n = len(wealth)
  if n == 0:
    return 0
  dp = [0] * (n + 1)
  dp[0] = wealth[0]
  dp[1] = wealth[1]
  for i in range(2, n ):
    dp[i] = max(wealth[i] + dp[i - 2], dp[i-1])

  return dp[n-1]



l = [2, 5, 1, 3, 6, 2, 4]
print(find_max_steal(l ) )

l = [2, 10, 14, 8, 1]
print(find_max_steal(l ) )