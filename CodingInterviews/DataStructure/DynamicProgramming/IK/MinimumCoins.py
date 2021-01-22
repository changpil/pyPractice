# Minimum Coins
#
# Given a variety of coin types defining a currency system,
# find the minimum number of coins required to express a given amount of money.
# Assume infinite supply of coins of every type.
#
# Example
# Input: Coin types: [1, 3, 5]. Amount to express: 9.
# Output: 3
# Here are all the unique ways to express 9 as a sum of coins 1, 3 and 5:
# 1, 1, 1, 1, 1, 1, 1, 1, 1
# 1, 1, 1, 1, 1, 1, 3
# 1, 1, 1, 1, 5
# 1, 1, 1, 3, 3
# 1, 3, 5
# 3, 3, 3
# Last two ways use the minimal number of coins, 3.

import math
def minimum_coins(coins, value):
    DP = [0]*(value + 1)
    for i in range(1, value + 1):
        result = math.inf
        for k in coins:
            if i - k > 0:
                result = min(result, DP[i-k] +1)
            elif i - k == 0:
                result = 1
        DP[i] = result
    return DP[-1]

print(minimum_coins([1,3,5], 9))