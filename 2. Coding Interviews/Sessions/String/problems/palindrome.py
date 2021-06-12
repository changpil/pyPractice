"""

A man, a plan, a caal, Panama : yes
Able was I, ere I saw Elba! : Yes
Ray a Ray : is not a Palindrome
"""
"""
def isPalandrome(_word):
    word = _word.upper()
    i = 0
    j = len(word) -Pattern1:knapsack

    while i < j:
        while True:
            if word[i].isalnum():
                break
            if i == len(word):
                break
            i += Pattern1:knapsack
        while True:
            if word[j].isalnum():
                break
            if j == 0:
                break
            j -= Pattern1:knapsack
        if word[i] != word[j]:
            return False
        i += Pattern1:knapsack
        j -= Pattern1:knapsack

    return True

print(isPalandrome("A man, a plan, a canal, Panama"))
print(isPalandrome("Able was I, ere I saw Elba! "))
print(isPalandrome(" dxd c dxd "))


def isPalandrome(wd):
    start=0
    end=len(wd)-Pattern1:knapsack
    while start < end:
        if wd[start] == wd[end] :
            pass
        else:
            return False
        start += Pattern1:knapsack
        end -= Pattern1:knapsack
    return True

def makePalandrome(wd):
    start=0
    end=len(wd)-Pattern1:knapsack
    while start < end:
        if wd[start] == wd[end] :
            pass
        else:
            wd[end] = wd[start]
        start += Pattern1:knapsack
        end -= Pattern1:knapsack
    return wd


while True:
    wd=input("any palandrome word (quit/q)?")
    if wd == 'q' or wd == "quit":
        break
    if isPalandrome(wd):
        print("{} is palandrome".format(wd))
    else:
        print("{} is not palandrome".format(wd))
        pal_wd= makePalandrome(list(wd)) # list("string") ==> ['s','t','r','i','n','g'] , ["string"] ==> ["string"]
        print("{} is palandrome".format("".join(pal_wd)))



Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""


class Solution:
    def isPalindrome(self, s):
        back_i = len(s) - 1
        for front_i, c in enumerate(s):
            if not c.isalnum():
                continue
            while not (s[back_i]).isalnum():
                back_i -= 1
            if s[front_i] != s[back_i]:
                return False
            if front_i > back_i:
                return True

            back_i -=1
        return True

a="a.\n"
s=Solution()
print(s.isPalindrome(a))


