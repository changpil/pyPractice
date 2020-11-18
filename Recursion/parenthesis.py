def balanced(testVariable, startIndex=0, currentIndex=0):
    if not testVariable:
        return False

    if startIndex >= len(testVariable):
        return True

    if testVariable[0] != "(":
        return False

    num_opened, num_closed = 1, 0
    i = startIndex + 1

    while i < len(testVariable) and num_closed != num_opened:
        if testVariable[i] == ")":
            num_closed += 1
        elif testVariable[i] == "(":
            num_opened += 1
        i += 1

    if num_opened != num_closed:
        return False

    return balanced(testVariable, i, i)

# Solution
def balanced(testVariable, startIndex = 0, opened = 0) :
  # Base case1 and 2
  if startIndex == len(testVariable) :
    return opened == 0

  # Base case3
  if opened < 0 : # A closing bracket did not find its corresponding opening bracket
    return False

  # Recursive case1
  if testVariable[startIndex] == "(" :
    return  balanced(testVariable, startIndex + 1, opened + 1)

  # Recursive case2
  elif testVariable[startIndex] == ")" :
    return  balanced(testVariable, startIndex + 1, opened - 1)


l = ["(",")","(",")",]
print(balanced(l))