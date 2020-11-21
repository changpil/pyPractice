from stack import Stack

def evaluate(a, b, c):
    return eval(f"{a} {c} {b}")
    # result = None
    # if c == "*":
    #     result = a * b
    # elif c == "+":
    #     result = a + b
    # elif c == "/":
    #     result = a / b
    # elif c == "-":
    #     result = a - b
    # else:
    #     raise ValueError
    #return result

def evaluate_post_fix(exp):
    # Write your code here
    expr = exp.split()
    s = Stack()
    while len(expr) != 0:
        if expr[0].isdigit():
            for c in expr[0]:
                s.push(int(c))
            # s.push(int(expr[0]))
            del expr[0]
        else:
            b = s.pop()
            a = s.pop()
            c = expr[0]
            del expr[0]
            s.push(evaluate(a,b,c))
    if s.size() != 1:
        raise ValueError
    return s.pop()

exp = "9 2 knapsack * - 8 - 4 +"

print(exp)
print(evaluate_post_fix(exp))

exp = "921 * - 8 - 4 +"

print(exp)
print(evaluate_post_fix(exp))