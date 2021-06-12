"""
Stock Buy and Sell Optimization (Medium)
Good morning, Chang! Here's our prompt for today.

This is a classic technical interview question that I've seen a number of times in real life interviews. Let's say you're given an array of stock prices, with each element being an integer that represents a price in dollars.

SNIPPET
[ 10, 7, 6, 2, 9, 4 ]
Each index of the array represents a single day, and the the element at that index is the stock price for that given day. This means that the array below represents:

JAVASCRIPT
const prices = [ 10, 7, 6, 2, 9, 4 ];
// Day 0 - a price of `$10`
// Day 1 - `$7`
// Day 2 - `$6` (and so on...)
Given the ability to only buy once and sell once, our goal is to maximize the amount of profit (selling price - purchase price) that we can attain and return that value. Note the only caveat is that that we cannot sell a stock before we buy it, which is important in identifying a solution.

Can you write a stock optimizer method called stockOptimizer? See the following examples for further clarification:

JAVASCRIPT
stockOptimizer([ 10, 7, 6, 2, 9, 4 ])
// 7
For the above example, the max profit is made when we buy on day/index 3 (when the price is 2) and sell on day/index 4 (when the price is 9). 9 - 2 gives us 7, which is returned by the function. Let's do another example.

JAVASCRIPT
stockOptimizer([9, 8, 6, 5, 3])
// 0
From a quick glance, it seems like there's enough price differences to generate a profit. However, notice that the price drops every day, and thus we can't have a profit since we're required to buy before selling.

Constraints
Length of the given array <= 100000
The array will always consist of non zero integer (including 0)
The maximum price would be <= 2147483647
Expected time complexity : O(n)
Expected space complexity : O(1)
The array would always contain more than 1 element
"""

def stockOptimizer(prices):
    _min= prices[0]
    profit = 0
    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - _min)
        _min = min(_min, prices[i])
    return profit

# prices = [0,1,2,3,4]
# print(stockOptimizer(prices))
# prices = [0,1,2,3,2]
# print(stockOptimizer(prices))
#
# prices = [1, 0, 2, 1, 4]
# print(stockOptimizer(prices))
# prices = [5,5,4,4,2]
# print(stockOptimizer(prices))
print(stockOptimizer([5,20,15,13,3,15,5,10])) #15
#assert stockOptimizer([5,20,15,13,3,15,5,10]) == 15