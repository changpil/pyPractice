"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
Example
                             #
            #              # # #
  #       # # #          # # # # #
            #              # # #
                             #
For n = 2, the output should be
shapeArea(n) = 5;
For n = 3, the output should be
shapeArea(n) = 13.
"""


def shapeArea(n):
    dp = [-1] * (n)
    dp[0] = 1
    dp[1] = 5
    for i in range(2, n):
        dp[i] = dp[i-1] + (i - 1) * 4 + 4

    return dp[n - 1]


print(shapeArea(2))
print(shapeArea(3))