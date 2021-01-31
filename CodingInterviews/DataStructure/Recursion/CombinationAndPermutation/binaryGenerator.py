# O(N)
def binaryString(n):
    result = ["0", "1"]

    for i in range(1, n):
        newP = []
        for s in result:
            newP.append(s+ "0")
            newP.append(s + "1")
        result = newP
    return result

print(binaryString(3))