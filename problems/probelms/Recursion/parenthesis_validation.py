
data={"[":"]","{":"}", "(":")"}

def parenthesis(_str):
    if len(_str) == 0 :
        return True
    i_char, num_i, first_i, last_i = "", 0, None, 0
    for i, c in enumerate(_str):
        if c == "(":
            i_char = c
            num_i += 1
            if first_i == None:
                first_i = i
        if c == ")":
            num_i -= 1
            rv=None
            if num_i == 0:
                last_i = i
                rv = parenthesis(_str[first_i+1:last_i])
                first_i =None
            if not rv:
                return False

    if num_i != 0:
        return False
    return True

#a="(()()(())())"
#print(parenthesis(a))
#Parenthesis Using stack

def parenthesis_stack(_str):
    s =list()
    try:
        for c in _str:
            if c == "(":
                s.append(c)
            elif c == ")":
                s.pop()
    except:
        return False
    if len(s) == 0:
        return True
    return False


a=")((()()(())())"
print(parenthesis_stack(a))