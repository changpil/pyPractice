# Robbery
#
# There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal value in these houses,
# but he cannot steal in two adjacent houses because the owner of a stolen house will tell his two neighbors on the left and right side.
# What is the maximal stolen value?
# For example, if there are four houses with values [6, 1, 2, 7], the maximal stolen value is 13, when the first and fourth houses are stolen.
#
# Example One
# Input: values = [6, 1, 2, 7]
# Output: 13
# Steal from the first and the last house.
#
# Example Two
# Input: values = [1, 2, 4, 5, 1]
# Output: 7
# Steal from the second and the fourth house.


def maxStolenValue(values):
    DP = [[0]*(len(values)) for _ in range(2)]
    DP[0][0] = values[0]
    DP[1][0] = 0
    print(DP)
    for i in range(1, len(values)):
        print(i)
        # include
        DP[0][i] = DP[1][i-1] + values[i]
        # exclude
        DP[1][i] = max(DP[0][i-1], DP[1][i-1])
    print(DP)
    return max(DP[0][-1], DP[1][-1])


#print(maxStolenValue([6,1,2,7]))
print(maxStolenValue([1,7]))