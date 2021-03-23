print("*"*10)
print("*  O(n) in-place")
print("*"*10)

def right_rotate(l, k):
    k = k%len(l)
    if k == 0:
        return l
    cache = l[len(l) - k:]
    for i in range(0,len(l) ,k):
        j = i
        jj = 0
        while j < len(l) and jj < k:
            cache[jj], l[j] = l[j], cache[jj]
            j += 1
            jj += 1
    return l

print(right_rotate([0,1,2,3,4], 2))
print(right_rotate([0,1,2,3,4], 4))
print(right_rotate([0,1,2,3,4, 5], 1))

print("*"*10)
print("*  O(n) out-of-place right shift")
print("*  slicing is O(n) ")
print("*"*10)


def right_rotate(l, k):
    k = k%len(l)
    # ll = l + l
    # return ll[len(l)-k:2*len(l) - k]
    return l[-k:] + l[:-k]

print(right_rotate([0,1,2,3,4], 2))
print(right_rotate([0,1,2,3,4], 4))
print(right_rotate([0,1,2,3,4, 5], 1))

print("*"*10)
print("*  O(n) out-of-place left shift")
print("*  slicing is O(n) ")
print("*"*10)


def right_rotate(l, k):
    k = k%len(l)
    #ll = l + l
    #return ll[k:len(l)+k]
    return l[k:] + l[:k]

print(right_rotate([0,1,2,3,4], 2))
print(right_rotate([0,1,2,3,4], 4))
print(right_rotate([0,1,2,3,4, 5], 1))