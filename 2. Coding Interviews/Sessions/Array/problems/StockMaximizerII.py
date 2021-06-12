"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""
# def stockOptimizer(prices):
#     _min= prices[0]
#     profit = 0
#     for i in range(1, len(prices)):
#         #print(_min, prices[i])
#
#         if prices[i-1] > prices[i]:
#             profit += prices[i-1] - _min
#             _min = prices[i]
#             # This was the wrong answer for [1,9,6,9,1,7,1,1,5,9,9,9]
#         #elif prices[i-1] < prices[i]:
#         else:
#             if i == len(prices) -1:
#                 profit += prices[i] - _min
#         print(profit)
#     return profit

def stockOptimizer(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit
# prices = [0,1,2,3,4]
# print(stockOptimizer(prices))
# prices = [0,1,2,3,2]
# print(stockOptimizer(prices))
#
# prices = [1, 0, 2, 1, 4]
# print(stockOptimizer(prices))
# prices = [5,5,4,4,2]
# print(stockOptimizer(prices))
print(stockOptimizer([5,20,15,13,3,15,5,10])) #32
print(stockOptimizer([1,9,6,9,1,7,1,1,5,9,9,9])) #25