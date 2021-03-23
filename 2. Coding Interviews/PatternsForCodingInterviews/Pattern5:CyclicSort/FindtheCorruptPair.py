# Find the Corrupt Pair (easy) #
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
#
# Example 1:
#
# Input: [3, 1, 2, 5, 2]
# Output: [2, 4]
# Explanation: '2' is duplicated and '4' is missing.
# Example 2:
#
# Input: [3, 1, 2, 3, 6, 4]
# Output: [3, 5]
# Explanation: '3' is duplicated and '5' is missing.


def find_corrupt_numbers(nums):
    i = 0
    result = []

    while i < len(nums):
        j = nums[i] - 1
        if i != j and nums[i] != nums[j]:
            nums[j], nums[i] = nums[i] , nums[j]
        else:
            i += 1

    for index , value in enumerate(nums):
        if index != value -1:
            result.extend([index+1, value])
    return result

def main():
    print(find_corrupt_numbers([3,1,2,5,2]))

main()