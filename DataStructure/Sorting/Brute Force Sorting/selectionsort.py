def sort(l):
    for i in range(len(l)):
        min_p = i
        for j in range(i, len(l)):
            if min(l[min_p], l[j]) == l[j]:
                min_p = j
        l[min_p], l[i] = l[i], l[min_p]


# Put the smallest element in the first place
# put the next smallest element in the next place

def i_selectionSort(l):
    for i in range(0, len(l)):
        min_index = i
        for j in range(i, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]


def r_selectionSort(l):
    _r_selectionSort(l, len(l) - 1)


def _r_selectionSort(l, n):
    if n == 0:
        return

    _r_selectionSort(l, n - 1)
    target = l[n]
    while n >= 1 and l[n - 1] > target:
        l[n] = l[n - 1]
        n -= 1
    l[n] = target


l = [9, 8, 7, 6, -3, 5, 4, 0, 3]

i_selectionSort(l)
print(l)

l = [9, 8, 7, -3, 5, 4, 0, 3]

r_selectionSort(l)
print(l)

l = [3,443,5,343,7,54,3]
sort(l)
print(l)