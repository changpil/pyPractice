# in_place
def remove_even1(list):
    for i in range(len(list)-1,-1,-1):
        if isinstance(list[i],int) and list[i]%2 == 0:
            del list[i]

l = [-144, 173, -108, -51, 102, -115, 146, -113, -183, 164, 27, 56, -75, -200, -106, -28, -36, 75, -68, -19, 54, -81, 143, -101]
remove_even1(l)
print(l)


# out-of-place
def remove_even1(list):
    return [num for num in list if num%2 != 0]

l = [-144, 173, -108, -51, 102, -115, 146, -113, -183, 164, 27, 56, -75, -200, -106, -28, -36, 75, -68, -19, 54, -81, 143, -101]
l = remove_even1(l)
print(l)