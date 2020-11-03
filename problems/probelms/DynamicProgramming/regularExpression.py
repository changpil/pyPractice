"""
Wildcard matching Dynamic programming
 No partial matching, complete machting

* = 0 or more
? = any one character

a*b = ab, aab, acb, axyb (True) b,a,ac abc(False)
a?b = aab, abb, acb (True) ab, b, cb (False)

"""
