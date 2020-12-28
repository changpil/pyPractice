# Word Break Count
#
# Given a dictionary of words and a string,
# find the number of ways the string can be broken down into the dictionary words. Return the answer modulo 10^9 + 7.
#
# Example
# Input: Dictionary: [“kick", "start", "kickstart", "is", "awe", "some", "awesome”]. String: “kickstartisawesome”.
# Output: 4
# Here are all four ways to break down the string into the dictionary words:
#
# kick start is awe some
# kick start is awesome
# kickstart is awe some
# kickstart is awesome
# 4 % 1000000007 = 4 so the correct output is 4.

# My first implementation; There was mistakes from ranges of arrays and indexes.
# def wordBreakCount(dictionary, txt):
#     DP = [0]*(len(txt)+1)
#     DP[0] = 1
#
#     for i in range(1, len(DP)):
#         for j in range(i + 1, len(DP)):
#             if txt[i-1:j] in dictionary and DP[i-1] != 0:
#                 DP[j] += DP[i-1]
#     return DP[-1]


def wordBreakCount(dictionary, txt):
    DP = [0]*(len(txt)+1)
    DP[0] = 1
    dset = set(dictionary)
    for i in range(1, len(DP) +1):
        for j in range(i + 1, len(DP)+1):
            if txt[i-1:j-1] in dset and DP[i-1] != 0:
                #print(f"{i -1}:{j -1} {txt[i - 1:j - 1]}" )
                DP[j-1] += DP[i-1]
                #print(DP)
    return DP[-1]


#dictionary = ['ki','ck','kick','start','kickstart']
#print(wordBreakCount(dictionary, "kickstart"))

# Answer 16
dictionary = ['a','aa','aaa','aaaa','aaaaa','aaaaa']
print(wordBreakCount(dictionary, "aaaaa"))