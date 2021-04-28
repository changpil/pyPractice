def evaluate(a, b, c):
    return eval(f"{a} {c} {b}")

def evaluate_post_fix(exp):
    # Write your code here
    expr = exp.split()
    s = []
    while len(expr) != 0:
        if expr[0].isdigit():
            for c in expr[0]:
                s.append(int(c))
            expr.pop(0)
        else:
            b = s.pop()
            a = s.pop()
            c = expr[0]
            expr.pop(0)
            s.append(evaluate(a,b,c))
    if len(s) != 1:
        raise ValueError
    return s[-1]

exp = "9 2 1 * - 8 - 4 +"

print(exp)
print(evaluate_post_fix(exp))

exp = "921 * - 8 - 4 +"

print(exp)
print(evaluate_post_fix(exp))