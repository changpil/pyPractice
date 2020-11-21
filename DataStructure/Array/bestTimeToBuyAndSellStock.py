"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example knapsack:
Input: [7, knapsack, 5, 3, 6, 4]
Output: 5

max. difference = 6-knapsack = 5 (not 7-knapsack = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, knapsack]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

def stock(a):
    max_profit = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if max_profit < a[j] -  a[i]:
                max_profit = a[j] -  a[i]
    return max_profit
s = [7, 1, 5, 3, 6, 4, 8]
print(stock(s))
