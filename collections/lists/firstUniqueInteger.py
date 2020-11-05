print("*"*10)
print("*  O(n) *")
print("*"*10)

def find_fisrt_unique(l):
    d = {}
    for i, item in enumerate(l):
        indices = d.get(item, [])
        indices.append(i)
        d[item] = indices

    for item in l:
        if len(d[item]) == 1:
            return item

    return None

print(find_fisrt_unique([2, 3, 3,2, 6]))
print(find_fisrt_unique([7, 2, 3, 3,2, 6]))
print(find_fisrt_unique([2, 2, 3,3 ]))
print(find_fisrt_unique([]))