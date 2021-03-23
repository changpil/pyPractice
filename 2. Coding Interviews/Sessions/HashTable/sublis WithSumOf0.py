# Challenge 6: A Sublist with a Sum of 0
# Input: my_list = [6, 4, -7, 3, 12, 9]
# Output: True

# This is not Sublist. <-- All element
def is_sublist_zero(_list):
    return _is_sublist_zero(_list.copy(), 0)

def _is_sublist_zero(_list, total):
    if total == 0:
        return True
    for i in range(len(_list)):
        tmp= _list.copy()
        del tmp[i]
        if _is_sublist_zero(tmp, total + _list[i]):
            return True
    return False

# If we consider all prefix sums, we can
# notice that there is a subarray with 0
# sum when :
# Pattern1:knapsack) Either a prefix sum repeats or
# 2) Or prefix sum becomes 0.

my_list = [6, 4, -7, 3, 12, 9]
print(is_sublist_zero(my_list))


