# Knight's tour!
# Given a phone keypad as shown below:
# 1 2 3
# 4 5 6
# 7 8 9
# – 0 –
# How many different phone numbers of given length can be formed starting from the given digit?
# The constraint is that the movement from one digit to the next is similar to the movement of the Knight in chess.
# For example if we are at 1 then the next digit can be either 6 or 8, if we are at 6 then the next digit can be 1, 7 or 0.
# Repetition of digits is allowed, e.g. 1616161616 is a valid number.
# The problem requires us to just give the count of different phone numbers and not necessarily list the numbers.
# Find a polynomial-time solution, based on Dynamic Programming.

# Example One
# Input: startdigit = 1, phonenumberlength = 2
# Output: 2
# Two possible numbers of length 2: 16, 18.
# Example Two
# Input: startdigit = 1, phonenumberlength = 3
# Output: 5
# The possible numbers of length 3: 160, 161, 167, 181, 183



def numPhoneNumbers(startdigit, phonenumberlength):

    nextNumber = {}
    nextNumber[0] = [4, 6]
    nextNumber[1] = [8, 6]
    nextNumber[2] = [7, 9]
    nextNumber[3] = [4, 8]
    nextNumber[4] = [0, 3, 9]
    nextNumber[5] = []
    nextNumber[6] = [0,1, 7]
    nextNumber[7] = [2, 6]
    nextNumber[8] = [1, 3]
    nextNumber[9] = [2, 4]


    DP = [[0]*(phonenumberlength + 1 ) for _ in range(10)]

    for i in range(10):
        DP[i][1] = 1

    for l in range(2, phonenumberlength + 1):
        for num in range(10):
            result = 0
            for next in nextNumber[num]:
                result += DP[next][l-1]
            DP[num][l] = result
    return DP[startdigit][-1]

print(numPhoneNumbers(0, 2))
print(numPhoneNumbers(0, 3))