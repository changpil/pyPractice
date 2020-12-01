def getDigits(num):
    arr =[]
    while num:
        num, digit = divmod(num, 10)
        arr.append(digit)
    rev = []
    for i in range(len(arr)-1, -1, -1):
        rev.append(arr[i])
    return rev

print(getDigits(23))
print(getDigits(23233))