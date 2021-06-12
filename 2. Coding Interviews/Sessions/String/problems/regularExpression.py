"""
Q1 )
wildcard only with * = 0 or 1
"""
def isMatch(s, pattern):
    if pattern.count("*") == 0:
        return s == pattern

    wildIndex = pattern.index("*")
    prefix = pattern[:wildIndex]
    postfix = pattern[wildIndex + 1:]

    if prefix and postfix:
        if s[:len(prefix)] != prefix:
            return False
        else:
            # prefix is matched So prefix was not available in s
            s = s[len(prefix):]
            return s[len(s) - len(postfix):] == postfix
    elif prefix:
        return s[:len(prefix)] == prefix
    else:
        return s[len(s) - len(postfix):] == postfix

# I failed the testcase of "cat", "cat*cat"
# print(isMatch("catcat", "cat*cat"))
# print(isMatch("cacat", "ca*at"))
# print(isMatch("catcat", "ca*at"))
# print(isMatch("cat", "cat*"))
#
# # False
# print(isMatch("cat", "cat*cat"))
# print(isMatch("cat", "cat*c"))

"""
Q2. If "*" has more than 1, how would you implement
"""

# Recursion and DP, what else Can I do?
print("#"*100)
def isMatchMoreWildCards(s, p):

    return _isMatchMoreWildCards(s, 0, p, 0)

# If you do not want to use space
# O(N) or O(X^2)
def _isMatchMoreWildCards(s, i, p, j):
    if len(s) == i:
        #"s" , "s**"
        while j + 1 < len(p) and p[j] == "*" and p[j+1] == "*":
                j += 1
        if len(p) == j or len(p) - 1 == j and p[j] == "*":
            return True
        else:
            return False
    if len(p) == j:
        return False
    if p[j] == "*":
        return _isMatchMoreWildCards(s, i+1, p, j) or _isMatchMoreWildCards(s, i, p, j+1)
    if s[i] != p[j]:
        return False
    return _isMatchMoreWildCards(s, i+1, p, j + 1)

# print(isMatchMoreWildCards("cs", "**c**s***"))
# print(isMatchMoreWildCards("catcat", "cat*cat*cat"))
# print(isMatchMoreWildCards("catssscatssscat", "cat*cat*cat"))
# print(isMatchMoreWildCards("catcat", "cat*cat*"))
# print(isMatchMoreWildCards("catcatssd", "cat*cat*"))
# print(isMatchMoreWildCards("ssacatcat", "*cat*cat"))
# print(isMatchMoreWildCards("catssscatssscat", "*cat*cat*"))
# print(isMatchMoreWildCards("cat", "cat*cat"))


def isMatchDP(s, p):

    # Normalize Pattern: Removing ***s***
    stack = []
    for c in p:
        if stack and stack[-1] == "*" and c == "*":
            continue
        else:
            stack.append(c)
    p = "".join(stack)

    dp = [[False]*(len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    if p[0] == "*":
        dp[0][1] = True

    for j in range(1, len(dp[0])):
        for i in range(1, len(dp)):
            if p[j-1] == "*":
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = False
    for l in dp:
        print(l)
    return dp[-1][-1]


print(isMatchDP("cs", "cs"))
print(isMatchDP("cs", "*"))
# print(isMatchDP("catcat", "cat*cat*cat"))
# print(isMatchDP("catssscatssscat", "cat*cat*cat"))
# print(isMatchDP("catcat", "cat*cat*"))
# print(isMatchDP("catcatssd", "cat*cat*"))
# print(isMatchDP("ssacatcat", "*cat*cat"))
# print(isMatchDP("catssscatssscat", "*cat*cat*"))
# print(isMatchDP("cat", "cat*cat"))