print("*"*10)
print("*  out-of--place *")
print("*"*10)
def merge_lists(lst1, lst2):
    # Write your code here
    m = []
    i, j = 0,0
    min_index = min(map(len, [lst1,lst2]))
    while i < min_index and j < min_index:
        if lst1[i] < lst2[j]:
            m.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            m.append(lst2[j])
            j += 1
        else:
            m.append(lst1[i])
            m.append(lst2[j])
            j += 1
            i += 1

    #if i < min_index:
    m.extend(lst1[i:])
    #if j < min_index:
    m.extend(lst2[j:])
    return m


l = merge_lists([],[1, 2, 3, 4, 5])
print(l)

l = merge_lists([1, 4, 45, 63],[])
print(l)

l = merge_lists([-133, -100, 0, 4],[-2000, 2000])
print(l)

l = merge_lists([],[])
print(l)

l = merge_lists([4, 4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4, 4])
print(l)

print("*"*10)
print("*  In-place *")
print("*"*10)
# In-Place
def merge_lists(lst1, lst2):
    i, j = 0,0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            i += 1
        else:
            lst1.insert(i, lst2[j])
            j += 1
            i += 1

    lst1.extend(lst2[j:])
    return lst1

l = merge_lists([],[1, 2, 3, 4, 5])
print(l)

l = merge_lists([1, 4, 45, 63],[])
print(l)

l = merge_lists([-133, -100, 0, 4],[-2000, 2000])
print(l)

l = merge_lists([],[])
print(l)

l = merge_lists([4, 4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4, 4])
print(l)