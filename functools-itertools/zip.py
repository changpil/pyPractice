students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


zipped = list(zip(*students))
print(zipped)
print(sorted(zipped[1]))


d = {i:i for i in range(10)}
s = sorted(set(d.keys()))
print(s)