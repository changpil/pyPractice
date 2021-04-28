#RadixSort is only Numbers

def radixSort(l):
    digits = len(str(l)) # same as getMaxdigits(l):
    buckets = [[] for i in range(10)]
    for digit in range(digits):
        for e in l:
            digit_e = getDigit(e, digit)
            buckets[digit_e].append(e)
        l = []
        for i in range(10):
            while len(buckets[i]) !=0:
                num = buckets[i].pop(0)
                l.append(num)


def getDigit(num, digit):
    mod = num
    for i in range(digit+1):
        num, mod = divmod(num, 10)
    return mod

def getMaxdigits(l):
    m = max(l)
    digit = 0
    while m !=0:
        m //= 10
        digit += 1
    return digit

l = [2,3,44,556,665]

radixSort(l)
print(l)