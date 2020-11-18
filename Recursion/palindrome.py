def isPalindrome(string):
    if string == None:
        return False
    if string == "":
        return True
    if len(string) == 1:
        return True

    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    else:
        return False

s = "hello"
print(s, end=" : ")
print(isPalindrome(s))

s = "hannah"
print(s, end=" : ")
print(isPalindrome(s))