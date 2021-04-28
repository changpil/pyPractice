
print("*"*10)
print("*  Solution1 O(n^2) *")
print("*"*10)

def sort(s):
    tmp = []
    while len(s) != 0:
        v = s.pop()
        while len(tmp) != 0 and tmp[-1] > v:
            s.append(tmp.pop())
        tmp.append(v)

    while len(tmp) != 0:
        s.append(tmp.pop())

s = [-3, 10, 4, 9]
sort(s)
print(s)


s = [-2, 0, 1, 4, 6, -1, 10]
sort(s)
print(s)

s = [23, 60, 12, 4, 97, 2]
sort(s)
print(s)