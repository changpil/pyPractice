#call stack size O(n) memory O(n)
def top_down(n):
    if n == 1:
        return 1
    return n * top_down(n-1)

def bottom_up(n):
    result = 1
    for i in range(n+1):
        result *=i
    return result

print(top_down(15))
