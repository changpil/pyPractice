"""
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Example

Index the array from . The number on each cloud is its index in the list so the player must avoid the clouds at indices  and . They could follow these two paths:  or . The first path takes  jumps while the second takes . Return .

Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

int c[n]: an array of binary integers
Returns

int: the minimum number of jumps required
"""
"""
Requirement Questions:
if index 0 is 1?
if there is no Path to jump?
"""
def jumpingOnClouds(clouds):
    dp = [-1]*len(clouds)
    dp[0] = 0
    if len(clouds) == 1:
        return 0
    for i in range(1, len(clouds)):
        if clouds[i] == 1:
            dp[i] = -1
            continue
        if i-2 >= 0 and dp[i-1] == -1 and dp[i-2] == -1:
            dp[i] = -1
        elif dp[i-1] == -1:
            dp[i] = dp[i-2] + 1
        elif dp[i-2] == -1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = min(dp[i-1], dp[i-2]) +1
    return dp [-1]
