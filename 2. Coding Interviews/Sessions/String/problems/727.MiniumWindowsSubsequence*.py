"""
Google
Input: str = "...a lot of people, be something, C algha, dghala, edhga, ftuggahaghaiafjgahalhk qafsl agagam afagnasfkhgs Ogahapqrhglaghashlh thgl uqlgha vagagh wagklha xaghhknmbv yaxbvmZ..."
                 -                -             -        -       -      -  -  -    -  -      -     -      -     -        -    ---       -    -    -      -              -          -     -
Output: substring which starts with 'a' and end with 'Z'
"""

# if(S[i] == T[j])
#     dp[i][j] = dp[i-1][j-1]
# else
#     dp[i][j] = dp[i-1][j]


def minWindows(S, T):
    ans = ''
    ls, lt = len(S), len(T)
    dp = [-1] * lt
    for x in range(ls):
        for y in range(lt - 1, -1, -1):
            if T[y] == S[x]:
                dp[y] = dp[y - 1] if y else x
                if y == lt - 1 and dp[-1] > -1:
                    _len = x - dp[-1] + 1
                    if not ans or _len < len(ans):
                        ans = S[dp[-1]: x + 1]
    return ans

str = "...a lot of people, be something, C algha, dghala, edhga, ftuggahaghaiafjgahalhk qafsl agagam afagnasfkhgs Ogahapqrhglaghashlh thgl uqlgha vagagh wagklha xaghhknmbv yaxbvmZ..."
str = str.lower()

print(minWindows(str, "abcdefghijklmnopqrstuvwxyz"))