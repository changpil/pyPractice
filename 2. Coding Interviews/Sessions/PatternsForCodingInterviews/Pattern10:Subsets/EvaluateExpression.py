# Evaluate Expression (hard) #
# Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.
#
# Example 1:
#
# Input: "1+2*3"
# Output: 7, 9
# Explanation: 1+(2*3) => 7 and (1+2)*3 => 9
# Example 2:
#
# Input: "2*3-4-5"
# Output: 8, -12, 7, -7, -3
# Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3

def diff_ways_to_evaluate_expression(input):
    return foo(input, 0, len(input)- 1)

def foo(expr, i, j):
    if i == j:
        return [int(expr[i])]

    if abs(i-j) == 2:
        return [eval(expr[i:j+1])]

    result = []
    for index in range(i , j+1):
        if expr[index] in ["+","-","*"]:
            r1 = foo(expr, i, index -1)
            r2 = foo(expr, index +1, j)
            result += comb(r1, r2, expr[index])
    return result

def comb(r1, r2, ex):
    func = None
    if ex == "*":
        func = lambda a,b: a*b
    elif ex == "+":
        func = lambda a,b: a+b
    elif ex == "-":
        func = lambda a, b: a-b
    result = []
    for i in range(len(r1)):
        for j in range(len(r2)):
            result.append(func(r1[i],r2[j]))
    return result

def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()