# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.
#
# Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.
#
# Write a function to return the next letter of the given ‘key’.

def search_next_letter(letters, key):
    i, j = 0, len(letters) -1

    while i <= j:
        mid = i + (j - i )//2

        if letters[mid] > key:
            j = mid -1
        elif letters[mid] < key:
            i = mid + 1
        else:
            if i == len(letters) -1:
                return letters[0]
            else:
                return letters[i +1]
    if i == len(letters):
        return letters[0]
    return letters[i]



def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()