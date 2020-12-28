# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
#
# Example 1:
#
# Input: N=2
# Output: (()), ()()
# Example 2:
#
# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()

from collections import deque
def generate_valid_parentheses(num):
    q = deque()
    q.append(["(", 1, 0])
    for _ in range(1, num*2):
        for _ in range(len(q)):
            tmp = q.popleft()
            tmp2 = tmp.copy()
            if tmp[1] + tmp[2] < num:
                tmp[0] += "("
                tmp[1] += 1
                q.append(tmp)
            if tmp2[1] > 0:
                tmp2[0] += ")"
                tmp2[1] -= 1
                tmp2[2] += 1
                q.append(tmp2)
    result = []
    while q:
        result.append(q.pop()[0])
    return result

def generate_valid_parentheses_recursive(num):
    result = []
    helper(num, 0, 0, "", result)

    return result
def helper(num, opened, closed, tmp, result):
    if closed ==  num:
        result.append(tmp)
        return
    if opened + closed < num:
        helper(num, opened + 1, closed, tmp + "(", result)
    if opened > 0:
        helper(num, opened - 1 , closed + 1, tmp + ")", result)

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))

  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses_recursive(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses_recursive(3)))
main()