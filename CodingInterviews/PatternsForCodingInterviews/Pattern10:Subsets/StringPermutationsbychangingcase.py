# Given a string, find all of its permutations preserving the character sequence but changing case.
#
# Example 1:
#
# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"
# Example 2:
#
# Input: "ab7c"
# Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

from collections import deque
def find_letter_case_string_permutations(str):
    q = deque()

    if str[0].isalpha():
        q.append([str[0].upper()])
        q.append([str[0].lower()])
    else:
        q.append([str[0]])

    for i in range(1, len(str)):
        for l in range(len(q)):
            tmp = q.popleft()
            if str[i].isalpha():
                tmp2 = tmp[:]
                tmp.append(str[i].upper())
                tmp2.append(str[i].lower())
                q.append(tmp)
                q.append(tmp2)
            else:
                tmp = tmp[:]
                tmp.append(str[i])
                q.append(tmp)
    return list(q)


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()