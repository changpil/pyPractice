
def minRemoveToMakeValid(s):
    return helper(s, 0, 0, 0, "")[1]

def helper(s, i, opened, closed, tmp):
    if opened < closed:
        return False, ""

    if len(s) == i:
        if opened == closed:
            return True, tmp
        else:
            return False, ""

    returnstr1, returnstr2 = None, None

    if s[i] == "(":
        returnstr1 = helper(s, i + 1, opened + 1, closed, tmp + "(")
        returnstr2 = helper(s, i + 1, opened, closed, tmp)
    elif s[i] == ")":
        returnstr1 = helper(s, i + 1, opened, closed + 1, tmp + ")")
        returnstr2 = helper(s, i + 1, opened, closed, tmp)
    else:
        returnstr2 = helper(s, i + 1, opened, closed, tmp + s[i])




    if returnstr1 != None and returnstr1[0] == True:
        return returnstr1


    return  returnstr2

print(minRemoveToMakeValid("lee(t(c)o)de)"))
#Time Limit Exceeded O(2^(num of Parenthesis)
#print(minRemoveToMakeValid("()ls)))(()(c()((((())(()))((()"))

def minRemoveToMakeValid(s):
    opened, closed = 0, 0
    stack = []
    for c in s:
        if c == ")" and opened == closed:
            continue
        elif c == "(":
            stack.append(c)
            opened += 1
        elif c == ")":
            stack.append(c)
            closed += 1
        else:
            stack.append(c)

    reStr = ""
    while stack:
        c = stack.pop()
        if c == "(" and opened > closed:
            opened -= 1
        else:
            reStr = c + reStr

    return reStr

print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid("))(("))
print(minRemoveToMakeValid("()ls)))(()(c()((((())(()))((()"))