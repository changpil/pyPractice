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

def generate_all_expressions(s, target):
    collection = list()
    tmp, eform = [] , []
    helper(s, target, 0, collection, tmp, eform)
    return collection


def helper(string, target, i, collection, expression, evalform):
    if i == len(string):
        if eval("".join(evalform)) == target:
            collection.append("".join(expression))
        return

    for n in range(i, len(string)):
        _substring = string[i:n + 1]
        expression.append(_substring)
        evalform.append(str(int(_substring)))
        if n + 1 == len(string) :
            helper(string,target, n + 1, collection,expression, evalform)
        else:
            expression.append("*")
            evalform.append("*")
            helper(string, target, n + 1 , collection, expression, evalform)
            expression.pop()
            evalform.pop()
            if eval("".join(evalform)) <= target:
                expression.append("+")
                evalform.append("+")
                helper(string, target, n +1 , collection, expression, evalform)
                expression.pop()
                evalform.pop()
        expression.pop()
        evalform.pop()

# 311 different expressions possible.
l = generate_all_expressions("05050505", 0)
pprint.pprint(l)
print(len(l))

# l = generate_all_expressions("6587412365875", 7412589630)
# pprint.pprint(l)
# print(len(l))
#
# l = generate_all_expressions("0000000000000", 0)
# pprint.pprint(l)
# print(len(l))