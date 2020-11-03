def plusOne(digits):
    """
    Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

    You may assume the integer do not contain any leading zero, except the number 0 itself.

    The digits are stored such that the most significant digit is at the head of the list.
    460 --> 460

    :type digits: List[int]
    :rtype: List[int]

    """
    carrier = 1
    for i in range(len(digits), 0, -1):
        i = i-1
        num = digits[i] + carrier
        digit = num % 10
        carrier = num // 10
        digits[i] = digit

    if carrier == 1:
        digits.insert(0, carrier)
    return digits


a=[0]
print(plusOne(a))