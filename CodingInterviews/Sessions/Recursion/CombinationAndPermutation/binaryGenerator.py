# O(N)
# def binaryString(n):
#     result = ["0", "1"]
#
#     for i in range(1, n):
#         newP = []
#         for s in result:
#             newP.append(s+ "0")
#             newP.append(s + "1")
#         result = newP
#     return result

def binaryString(n):
    tmp, store = [], []
    helper(n, tmp, store)
    return store

def helper(n, tmp, store):
    if n == 0:
        store.append("".join(tmp))
        return

    tmp.append("0")
    helper(n-1, tmp, store)
    tmp.pop()
    tmp.append("1")
    helper(n - 1, tmp, store)
    tmp.pop()

print(binaryString(3))