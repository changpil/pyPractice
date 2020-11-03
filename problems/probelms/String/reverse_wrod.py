"""
Reverse the words in string eg. 'The Sky is Blue'. then print 'Blue is Sky The'.

"""

def reverse(wd):
    s=wd.split()
    s.reverse()
    return " ".join(s)

print(reverse("The Sky is Blue"))