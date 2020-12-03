# Problem Statement #
# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
#
# Example 1:
#
# Input: 23
# Output: true (23 is a happy number)
# Explanations: Here are the steps to find out that 23 is a happy number:

# Input: 12
# Output: false (12 is not a happy number)
# Explanations: Here are the steps to find out that 12 is not a happy number:

def getNextDigits(num):
    total = 0
    while num:
        num, remainer= divmod(num, 10)
        total += remainer**2
    return total

# My implementation
# def find_happy_number(num):
#     s = set()
#     while num != 1:
#         if num in s:
#             return False
#         s.add(num)
#         num = getNextDigits(num)
#     return True

#Educative implementation
def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = getNextDigits(slow)  # move one step
    fast = getNextDigits(getNextDigits(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'

print(find_happy_number(23))
print(find_happy_number(12))
print(find_happy_number(13))
print(find_happy_number(71))
print(find_happy_number(37))
print(find_happy_number(41))
print(find_happy_number(43))
print(find_happy_number(47))
print(find_happy_number(51))
print(find_happy_number(57))
print(find_happy_number(63))
print(find_happy_number(67))