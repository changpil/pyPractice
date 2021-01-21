# Generate All Possible Expressions That Evaluate To The Given Target Value
# Generate All Possible Expressions That Evaluate To The Given Target Value
#
# Given a string s that consists of digits (“0”..”9”) and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.
# When building expressions, you have to insert one of the following operators between each pair of consecutive characters in s: “join” or “*” or “+”. For example, by inserting different operators between the two characters of string “12” we can get either 12 (1 joined with 2) or 2 (1*2) or 3 (1+2).
# Other operators such as “-” or “÷” are NOT supported.
# Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.
# Precedence of the operators is conventional: “join” has the highest precedence, “*” – medium and “+” has the lowest precedence. For example, 1+2*34=(1+(2*(34)))=1+68=69.
#
# You have to return ALL expressions that can be built from string s and evaluate to the target.
#
# Example One
# Input:
# s="222", target=24.
#
# Output:
# ["22+2", "2+22"] and ["2+22", "22+2"] are both correct outputs.
# 22+2=24: we inserted the “join” operator between the first two characters and the “+” operator between the last two characters of s.
# 2+22=24: we inserted the “+” operator between the first two characters and the “join” operator between the last two characters of s.
#
# Example Two
# Input: s="1234", target=11.
#
# Output: ["1+2*3+4"]
#
# Example Three
# Input:
# s="99", target=1.
#
# Output:
# []




import pprint

# def generate_all_expressions(s, target):
#     collection, tmp = list(), ""
#     helper(s, target, collection, tmp)
#     return list(set(collection))
#
#
# def helper(s, target, collection, tmp):
#     if s == "":
#         if eval(tmp[:-1]) == target:
#             collection.append(tmp[:-1])
#         return
#
#     # In the case of 0 + 5*3* and the next is 0.
#     #if tmp != "" and eval(tmp[:-1]) > target:
#     #    return
#
#     for i in range(len(s)):
#         helper(s[i + 1:], target, collection, tmp + str(int(s[:i + 1])) + "+")
#         helper(s[i + 1:], target, collection, tmp + str(int(s[:i + 1])) + "*")


# l = generate_all_expressions("050505", 5)
# pprint.pprint(l)
# print(len(l))


# This solution has time complexcity issues 68% success rate
# def generate_all_expressions(s, target):
#     collection = list()
#     helper(s, target, collection, "", "")
#     return collection
#
#
# def helper(s, target, collection, tmp, eform):
#     if s == "":
#         if eval(eform) == target:
#             collection.append(tmp)
#         return
#
#     for i in range(len(s)):
#         if tmp == "":
#             helper(s[i + 1:], target, collection, s[:i + 1] , str(int(s[:i + 1])) )
#         else:
#             if eval(eform) <= target:
#                 helper(s[i + 1:], target, collection, tmp + "+" + s[:i + 1], eform + "+" + str(int(s[:i + 1])) )
#             helper(s[i + 1:], target, collection, tmp + "*" + s[:i + 1], eform + "*" + str(int(s[:i + 1])) )



# l = generate_all_expressions("22", 4)
# pprint.pprint(l)
# print(len(l))
#
# l = generate_all_expressions("050505", 5)
# pprint.pprint(l)
# print(len(l))
#
#
# l = generate_all_expressions("1234", 11)
# pprint.pprint(l)
# print(len(l))


# l = generate_all_expressions("6666666666666", 6)
# pprint.pprint(l)
# print(len(l))
#
#
# l = generate_all_expressions("0123456789012", 123456789012)
# pprint.pprint(l)
# print(len(l))


# Timeout
# def generate_all_expressions(s, target):
#     collection = list()
#     tmp, eform = [] , []
#     helper(s, target, 0, collection, tmp, eform)
#     return collection
#
#
# def helper(string, target, i, collection, expression, evalform):
#     if i == len(string):
#         if eval("".join(evalform)) == target:
#             collection.append("".join(expression))
#         return
#
#     for n in range(i, len(string)):
#         _substring = string[i:n + 1]
#         expression.append(_substring)
#         evalform.append(str(int(_substring)))
#         if n + 1 == len(string) :
#             helper(string,target, n + 1, collection,expression, evalform)
#         else:
#             expression.append("*")
#             evalform.append("*")
#             helper(string, target, n + 1 , collection, expression, evalform)
#             expression.pop()
#             evalform.pop()
#             if eval("".join(evalform)) <= target:
#                 expression.append("+")
#                 evalform.append("+")
#                 helper(string, target, n +1 , collection, expression, evalform)
#                 expression.pop()
#                 evalform.pop()
#         expression.pop()
#         evalform.pop()
#
# # 311 different expressions possible.
# l = generate_all_expressions("05050505", 0)
# pprint.pprint(l)
# print(len(l))

# l = generate_all_expressions("6587412365875", 7412589630)
# pprint.pprint(l)
# print(len(l))
#
# l = generate_all_expressions("0000000000000", 0)
# pprint.pprint(l)
# print(len(l))


def generate_all_expressions(s, target):
    if not s:
        return []

    output = []
    foo(s, target, 0, "", 0, 0, output)
    return output


def foo(s, target, i, tmp, val, prev, output):
    if i == len(s):
        if val == target:
            output.append(tmp)
        return

    for end in range(i + 1, len(s)+1):
        cur = s[i:end]
        cur_int = int(cur)

        if i == 0:
            foo(s, target, end, cur, cur_int, cur_int, output)
        else:
            foo(s, target, end, tmp + "+" + cur, val + cur_int, cur_int, output)
            foo(s, target, end, tmp + "*" + cur, val - prev + (prev * cur_int), prev * cur_int, output)

l = generate_all_expressions("05050505", 0)
# l = generate_all_expressions("222", 8)
pprint.pprint(l)
print(len(l))

# l = generate_all_expressions("6587412365875", 7412589630)
# pprint.pprint(l)
# print(len(l))
#
# l = generate_all_expressions("0000000000000", 0)
# pprint.pprint(l)
# print(len(l))