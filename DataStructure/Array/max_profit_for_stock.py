"""
list is stock price for a given day.

[23, 24, 25, 18, 19, 23, 24, 27, 29, 30]
[23, 22, 21, 18, 19, 23, 24, 27, 29, 30]
"""

"""
Q1
What is the maximum profits that can be made by buying and selling a share a time over a given day range. 
"""

def maxprofit_for_one_tansaction(_list):

    maxprofit = 0
    for i , p in enumerate(_list):
        for j in range(i+1, len(_list)):
            maxprofit = max(maxprofit, _list[j] - p)  # Mistake: p - _list[j]
    return maxprofit if maxprofit > 0 else 0


a =[23, 24, 25, 18, 19, 23, 24, 27, 29, 30]
print(a)
print(maxprofit_for_one_tansaction(a))

"""
Q3
What is the maximum profits that can be made by buying and selling a share k times over a given day range. 
When new transaction can only start after previous transaction is complete.
Let profit[t][i] represent maximum profit using at most t transactions up to day i (including day i). Then the relation is:

profit[t][i] = max(profit[t][i-Pattern1:knapsack], max(price[i] – price[j] + profit[t-Pattern1:knapsack][j]))
          for all j in range [0, i-Pattern1:knapsack]
profit[t][i] will be maximum of –

profit[t][i-Pattern1:knapsack] which represents not doing any transaction on the ith day.
Maximum profit gained by selling on ith day. In order to sell shares on ith day, we need to purchase it on any one of [0, i – Pattern1:knapsack] days. 
If we buy shares on jth day and sell it on ith day, max profit will be price[i] – price[j] + profit[t-Pattern1:knapsack][j] where j varies from 0 to i-Pattern1:knapsack. 
Here profit[t-Pattern1:knapsack][j] is best we could have done with one less transaction till jth day.     
"""
import pprint
def maxprofit_for_k_tansactions(_prices, k):
    _profits = [[0 for i in range(len(_prices))] for j in range(k+1)]

    for t  in range(1, k+1):
        for i in range(1, len(_prices)):
            maxprofit = 0
            for j in range(0, i ):
                maxprofit = max(maxprofit, _prices[i] - _prices[j]+ _profits[t-1][j])
            _profits[t][i] = max(_profits[t][i-1], maxprofit)

    pprint.pprint(_profits)
    return _profits[k][len(_prices)-1];

print(maxprofit_for_k_tansactions(a, 3))

"""
Q4
What is the maximum profits that can be made by buying and selling a share any time over a given day range. 
When new transaction can only start after previous transaction is complete.
"""
def max_profits(_list):
    profit=0

    for i in range(1, len(_list)):
        delta = _list[i] - _list[i-1]
        profit +=  delta if delta > 0 else 0
    return profit

print(max_profits(a))
