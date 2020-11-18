def i_insertionSort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i
        while j > 0 and key < l[j-1]:
            l[j] = l[j-1]
            j -= 1
        l[j] = key


def sort(testVariable, length) :
	if length < 1:
		return

	sort(testVariable, length -1)
	key = testVariable[length-1]
	i = length - 2
	while i >= 0  and testVariable[i] > key:
		testVariable[i], testVariable[i+1] = testVariable[i+1], testVariable[i]
		i -= 1
	testVariable[i+1] = key

l=[9,8,7,6,5,4,3]
sort(l)
print(l)
