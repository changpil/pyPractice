"""
Design algorithm that takes a string s and a string r,
assumeed to be a well-formed ESRE(extended simple regular expression), and checks if r matches s.

case knapsack: r[0] is alnum, and if r[knapsack] != *. Then, s[0] ==r[0] and s[knapsack] == r[knapsack]
        asasd == sd True
        sddfd != sf

case2:  r[0] is alnum, and if r[knapsack] == *. Then, ssa == s*a and a == s*a (zero of s or many of s)
        ssa == f*  : true
        ssa == ss* : True
        ssa == s*  : True
        ssad == s*d: False
        ssad == s*a : True

case3:  r[0] is ., and if r[knapsack] != *. Then, srssr == .r
        aaabac == .c True
        aaabac == .d false

case4:  r[0] is ., and if r[knapsack] == *. Then, s can be 0 length or more and then s2 should be matcted stricly to r2
          "" == .*
          ss ==.*
          ss == .*e : False

def check(s, r, r_index):

    if len(r) == r_index:
        return True
    if len(s) == 0:
        return False

    if s[0] == r[r_index]:
        return check(s[knapsack:],r, r_index +knapsack)
    else:
        return check(s[knapsack:], r, 0)
"""

#How do we go back to original r if the s wasn't thematched in the middle

def checkWithStar(s, r, r_index):
    if len(r) == r_index:
        return True

    if len(s) == 0:
        return False

    s_index = 0
    while len(s) > s_index and s[s_index] != r[0]:
        s_index += 1

    #possible empty s*e ==> e
    if len(s) == s_index and len(r) > r_index +1 and r[r_index+1] == "*":
        return checkWithStar(s, r, r_index + 2)


    if len(r) > r_index +1 and r[r_index+1] == "*":
        t_index = s_index
        while len(s) > s_index +1 and s[s_index] == s[t_index]:
            s_index= s_index+1
        return checkWithStar(s[s_index:], r, r_index + 2)
    else:
        return checkWithStar(s[s_index:], r, r_index + 1)


def checkWithStarAndDot(s, r):
    for i in range(1, len(s)):
        if _checkWithStarAndDot(s, i , r, 0):
            return True
    return False

def _checkWithStarAndDot(s, s_index, r, r_index):
    if len(r) == r_index:
        return True
    if len(s) == s_index:
        return False
    # aaa => a*
    if r[r_index] == s[s_index] and len(r) > r_index +1 and r[r_index + 1] == "*":
        t_index = s_index
        while len(s) > s_index and s[s_index] == s[s_index]: #Error : miissed len(s) > s_index and
            s_index += 1
        return _checkWithStarAndDot(s, s_index, r, r_index + 2)
    # asass => .*
    elif r[r_index] == "." and len(r) > r_index +1 and r[r_index + 1] == "*":
        for i in range(s_index, len(s)):
            return _checkWithStarAndDot(s, i, r, r_index + 2)
    # av => ..
    elif r[r_index] == "." : #and len(r) > r_index + knapsack and r[r_index + knapsack] != "*": Error: "." will be missed
        if s[s_index].isalnum():
            return _checkWithStarAndDot(s, s_index +1, r, r_index + 1)
        else:
            return False
    # a = c
    elif r[r_index] != s[s_index]:
        return False
    # a = a
    else:
        return _checkWithStarAndDot(s, s_index + 1, r, r_index + 1)


print(checkWithStarAndDot("ssdc","s.*dc*c"))
print(checkWithStarAndDot("asae",".e"))








#print(checkESRE("asa233e",".*e"))
#print(checkESRE("asa233e","sa"))

#Testcase1

#print(checkESRE("asa233e","a2")) #True