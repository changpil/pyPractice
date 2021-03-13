def isValidSubsequence(array, sequence):
	if len(array) < len(sequence):
		return False
	i, j = 0,0
	while i < len(array):
		if j < len(sequence) and array[i] == sequence[j]:
			j += 1
		i += 1
	return True if j == len(sequence) else False

array =  [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 23, 6, -1, 8, 10]
print(isValidSubsequence(array, sequence))