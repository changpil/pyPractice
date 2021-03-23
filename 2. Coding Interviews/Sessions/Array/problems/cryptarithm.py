"""
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

"""

def isCryptSolution(crypt, solution):
    mapper = {}
    for items in solution:
        mapper[items[0]] = items[1]
    nums= [""]*3
    i = 0
    for num in crypt:
        for c in num:
            nums[i] = nums[i] + mapper[c]
        i += 1
    for num in nums:
        if isLeadingZero(num):
            return False

    if int(nums[0]) + int(nums[1]) == int(nums[2]):
        return True
    return False

def isLeadingZero(num):
    if num[0] == '0' and len(num)!= 1:
        return True
    return False

crypt= ["SEND", "MORE", "MONEY"]
solution= [["O","0"], ["M","1"], ["Y","2"], ["E","5"], ["N","6"], ["D","7"], ["R","8"], ["S","9"]]

print(isCryptSolution(crypt, solution))
#
crypt=["TEN", "TWO", "ONE"]
solution = [["O","1"], ["T","0"], ["W","9"], ["E","5"], ["N","4"]]
print(isCryptSolution(crypt, solution))