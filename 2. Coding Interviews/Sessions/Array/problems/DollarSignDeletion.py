"""
You're given an array of strings containing alphabetical characters and certain $ characters. A $ represents a DELETE action whereby the character before it is deleted.

Each of these strings will be run through a method to operate on the $ DELETE action. We want to find out if the final string is the same for all of them. Let's take an example:

Example:
    const input = ["f$st", "st"]
    isDollarDeleteEqual(input);
    // true
    // true because both become "st"


Expected overall time complexity : O(n)
Expected space complexity : O(n)
"""


def is_dollar_delete_equal(arr):
    chs = [None]*len(arr)
    for i in range(len(arr)):
        ch = deleteDollar(arr[i])
        if i != 0:
            if ch != chs[i-1]:
                return False
            else:
                chs[i] = ch
        else:
            chs[i] = ch
    return True

def deleteDollar(s):
    stack = []
    for c in s:
        if c == '$':
            if len(stack) == 0:
                continue
            else:
                stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
    # try:
    #     while True:
    #         i = s.index("$")
    #         if i == 0:
    #             s = s[i + 1:]
    #         else:
    #             s = s[:i-1] + s[i+1:]
    # except:
    #     return s

input = ["f$st", "st"]
print(is_dollar_delete_equal(input))
input =  ['a90$n$c$se', 'a90n$cse']
print(is_dollar_delete_equal(input))
input =  ['ab$$', 'c$d$']
print(is_dollar_delete_equal(input))
input =  ['b$$p', '$b$p']
print(is_dollar_delete_equal(input))
