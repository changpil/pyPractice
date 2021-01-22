from collections import deque


def addStrings(num1, num2):
    h = {}
    for digit, ch in enumerate("0123456789"):
        h[ch] = digit

    n1 = 0

    for ch in num1:
        n1 = n1 * 10 + h[ch]

    n2 = 0
    for ch in num2:
        n2 = n2 * 10 + h[ch]

    s = n1 + n2
    # Miss s == 0.
    if s == 0:
        return "0"

    d = deque()
    r = {i: ch for ch, i in h.items()}

    while s:
        s, div = divmod(s, 10)
        d.appendleft(r[div])
    return "".join(d)

print(addStrings("0", "0"))