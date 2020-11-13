def validate(value):
    stack = []
    _dict = {"(": ")", "[": "]", "{": "}"}
    try:
        for i in value:
            print(i)
            print(stack)
            if i in list(_dict.keys()):
                stack.append(i)
            elif i in list(_dict.values()):
                p = stack.pop()
                if i != _dict[p]:
                    return False
    except IndexError:
        return False

    if len(stack) != 0:
        return False
    return True

print(validate("{}"))