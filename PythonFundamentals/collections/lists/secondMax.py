print("*"*10)
print("*  O(n) *")
print("*"*10)

def find_second_maximum(lst):
    first_max, second_max = float("-inf"),  float("-inf")
    for item in lst:
        if first_max < item:
            second_max = first_max
            first_max = item
        elif second_max < item < first_max:
            second_max = item
    return None if second_max == float("-inf") else second_max

print(find_second_maximum([9, 2, 3, 6]))
print(find_second_maximum([4, 2, 1, 5, 0]))
print(find_second_maximum([9, 9,-2,-2]))
print(find_second_maximum([9]))
print(find_second_maximum([]))