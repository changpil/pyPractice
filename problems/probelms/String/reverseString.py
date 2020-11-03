def reverseString( s):
    """
    :type s: str
    :rtype: str
    """
    rv = list(s)
    rv.reverse()
    return "".join(rv)

a="123456789 123456789 \n 123456789"
print(reverseString(a))