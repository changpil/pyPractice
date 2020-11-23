# Problem Statement #
# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.
#
# Example 1:
#
# Number of stairs (n) : 3
# Number of ways = 4
# Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3}
# Example 2:
#
# Number of stairs (n) : 4
# Number of ways = 7
# Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1},
# {2,2}, {1,3}, {3,1}

def staircases(n):
    if n == 0:
        return 1
    if n <0:
        return 0

    total = 0

    for i in range(1, 4):
        total += staircases(n -i)
    return total

print(staircases(3))
print(staircases(4))
print(staircases(5))