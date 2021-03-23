
# Test For tie with weights as inputs
# sum(G1) == sum(G2)
# result: True/False
# inputs = [w0, w1, w2, w3,w4,w5, ...]
# f(i, sum) = f(i+1, sum-weights[i]) || f(i+1, sum)

# def canSplitTheSameWeight(weights):
#     totalsum = sum(weights)
#     if totalsum%2 != 0:
#         return False
#     halfsum = totalsum//2
#
#     dp = [[False]*(halfsum +1) for _ in range(len(weights) +1)]
#
#     for i in range(len(weights) + 1):
#         dp[i][0] = True
#
#     for i in range(len(weights)-1, -1, -1):
#         for s in range(1, halfsum + 1):
#             result = False
#             if s >= weights[i]:
#                 result = dp[i+1][s - weights[i]]
#             dp[i][s] = result or dp[i+1][s]
#     # for i in range(len(dp)):
#     #     print(dp[i])
#     return dp[0][halfsum]

def canSplitTheSameWeight(weights):
    totalsum = sum(weights)
    if totalsum%2 != 0:
        return False
    halfsum = totalsum//2

    dp = [[False]*(halfsum +1) for _ in range(len(weights))]

    for i in range(len(weights)):
        dp[i][0] = True

    for i in range(len(weights)):
        for s in range(1, halfsum + 1):
            if s >= weights[i]:
                dp[i][s] = dp[i-1][s - weights[i]]
            dp[i][s] = dp[i][s] or dp[i-1][s]
    # for i in range(len(dp)):
    #     print(dp[i])
    return dp[-1][-1]

# True 22/2 = 11
weights =[1,2,3,4,5,7]
print(canSplitTheSameWeight(weights))

# True 16/2 = 8
weights =[1,3,5,7]
print(canSplitTheSameWeight(weights))

#False 12/2 = 6
weights =[2, 2 ,8]
print(canSplitTheSameWeight(weights))

# weights =[1,3,4,5,17]
# print(canSplitTheSameWeight(weights))