"""
reverse integer

321 => 123
-12 => -21
-120 =>-21
"""


def reverse(num):
    if num < 0:
        negative = True
    s_num=str(abs(num))
    reverse_num = s_num[::-1]
    return int(reverse_num) if negative is not True else int(reverse_num)*-1


print(reverse(-120001))
