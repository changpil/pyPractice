# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.
#
# Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:
#
# Items: { Apple, Orange, Melon }
# Weights: { 1, 2, 3 }
# Profits: { 15, 20, 50 }
# Knapsack capacity: 5
#
# Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5.
#
# 5 Apples (total weight 5) => 75 profit
# 1 Apple + 2 Oranges (total weight 5) => 55 profit
# 2 Apples + 1 Melon (total weight 5) => 80 profit
# 1 Orange + 1 Melon (total weight 5) => 70 profit
#
# This shows that 2 apples + 1 melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

def knapsack(p, w, c):
    """

    :param w: weights [int]
    :param p: profits [int]
    :param c: capacity int
    :return:
    """
    return _knapsack(p, w , c, 0, 0)

def _knapsack(p, w, c, weight, profit):
    if weight > c:
        return 0
    if weight + min(w) > c:
        return profit

    max_profit = 0
    for i in range(len(w)):
        max_p = _knapsack(p, w, c, weight + w[i], profit + p[i])
        max_profit = max(max_profit, max_p)

    return max_profit

print(knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))

# Brute Force in educative
def knapsack(p, w, c, i = 0):
    """

    :param w: weights [int]
    :param p: profits [int]
    :param c: capacity int
    :return:
    """
    if i >= len(w) or c < 0:
        return 0

    profit1 = 0
    # What is the difference for this condition?
    if w[i] <= c:
        # print(f"{i}  {c}", end= " ")
        profit1 = p[i] + knapsack(p, w, c - w[i], i)
    profit2 = knapsack(p, w, c, i + 1)
    return max(profit1, profit2)

print(knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


