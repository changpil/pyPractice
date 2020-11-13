print("*"*10)
print("*  O(n) in-place rearrage negative and positive")
print("*"*10)

def rearrange(lst):
    pivot, i = 0, 0
    while i < len(lst):
        if lst[i] >= 0:
            i += 1
        else:
            lst[i], lst[pivot] = lst[pivot], lst[i]
            pivot += 1
            i += 1
    return lst

print(rearrange([-1, 2, -3, -4, 5]))
print(rearrange([300, -1, 3, 0]))
print(rearrange([0, 0, 0, -2]))

print("*"*10)
print("*  O(n) out-of-place rearrage negative and positive")
print("*"*10)

def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

print(rearrange([-1, 2, -3, -4, 5]))
print(rearrange([300, -1, 3, 0]))
print(rearrange([0, 0, 0, -2]))


print("*"*10)
print("*  O(n) in-place rearrage negative and positive eith mid zeros")
print("*"*10)

def rearrange(lst):
    zero_i, pos_i, i = 0, 0, 0
    while i < len(lst) - zero_i:
        if lst[i] > 0:
            i += 1
        elif lst[i] < 0:
            lst[i], lst[pos_i] = lst[pos_i], lst[i]
            pos_i += 1
            i += 1
        else:
            lst[i], lst[len(lst) - 1 - zero_i] = lst[len(lst) - 1 - zero_i] , lst[i]
            zero_i += 1
    for i in range(zero_i):
        lst[pos_i], lst[len(lst)-1-i] = lst[len(lst)-1-i],lst[pos_i]
        pos_i += 1
    return lst

print(rearrange([-1, 2, -3, -4, 5]))
print(rearrange([300, -1, 3, 0]))
print(rearrange([0, 0, 0, -2]))
print(rearrange([300,0,  -1, 3, 0]))