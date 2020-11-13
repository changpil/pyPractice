print("*"*10)
print("*  O(n) *")
print("*"*10)
def find_product(l):
    zero_indices = []
    product = 1
    for i in range(len(l)):
        if l[i] == 0:
            zero_indices.append(i)
        else:
            product *= l[i]

    if len(zero_indices) > 1:
        return [0 for _ in range(len(l))]
    if len(zero_indices) == 1:
        return [product if i == zero_indices[0] else 0 for i in range(len(l))]
    arr = []
    for i in range(len(l)):
        arr.append(product//l[i])

    return arr

print(find_product([1,2,3,4]))
print(find_product([]))
print(find_product([1,2,0,4]))
print(find_product([0,2,0,4]))