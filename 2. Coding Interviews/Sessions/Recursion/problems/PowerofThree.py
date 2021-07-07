"""
Given an integer num, write a method to determine if it is a power of 3.


The method will be called as follows:

JAVASCRIPT
console.log(powerOfThree(9));
// true

console.log(powerOfThree(7));
// false
Constraints
The given would be a non zero positive integer in the range between 1 and 2147483647
Expected space complexity : O(logn)
Expected time complexity : O(1)
"""

# Time Limit Exceed O(log3 N)
# def power_of_three(num):
#     if num == 1:
#       return True
#     if num < 0:
#         return False
#     while num != 1:
#         num, div = divmod(num,3)
#         if div != 0:
#             return False
#     return True
def power_of_three(num):
    if num == 1:
      return True
    if num < 0:
        return False
    m_maxint = 3**30
    return m_maxint%num == 0


print(power_of_three(9))
print(power_of_three(27))
print(power_of_three(24))
print(power_of_three(45))
print(power_of_three(729))