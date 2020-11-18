# 42 can be completely divided by 11, 22, 33, 66, 77, 14, 21 and 42.
# 56 can be completely divided by 11, 22, 44, 77, 88, 14, 28 and 56.
# Therefore the greatest common divisor of 4242 and 5656 is 1414.

# Brute Force way

# def gcd(_list1, _list2):
#     smallest = min(_list1, _list2)
#     r = _gcd(_list1, _list2, smallest)
#     return r
#
#
# def _gcd(v1, v2, smaller):
#     if smaller == 1:
#         return 1
#
#     if v1 % smaller == 0 and v2 % smaller == 0:
#         return smaller
#
#     return _gcd(v1, v2, smaller - 1)

# print("gcd(14, 30)")
# print(gcd(14, 30))


# gcd = m if m == n
#       gcd( m-n, m) if m > n,
#       gcd( n, n-m ) if m < n,
def gcd(m, n):
    if m == n:
        return m

    if m > n:
        return gcd(m - n, n)
    else:
        return gcd(m, n-m)

print("gcd(14, 30)")
print(gcd(14, 30))