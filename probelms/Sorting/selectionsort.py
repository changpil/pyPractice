def sort(l):
    for i in range(len(l)):
        min_p = i
        for j in range(i, len(l)):
            if min(l[min_p], l[j]) == l[j]:
                min_p = j
        l[min_p], l[i] = l[i], l[min_p]

l = [3,443,5,343,7,54,3]
sort(l)
print(l)