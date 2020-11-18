# Put the smallest element in the first place
# put the next smallest element in the next place

def i_selectionSort(l):
    if not l:
        return
    for i in range(len(l)):
        min, min_index = l[i], i
        for j in range(i+1, len(l)):
            if l[j] < min:
                min, min_index = l[j], j

        l[i], l[min_index] = l[min_index], l[i]



l = [9, 8, 7, 6, -3, 5, 4, 0, 3]

i_selectionSort(l)
print(l)

# l = [9, 8, 7, -3, 5, 4, 0, 3]
#
# r_selectionSort(l)
# print(l)
#
# l = [3,443,5,343,7,54,3]
# i_selectionSort(l)
# print(l)