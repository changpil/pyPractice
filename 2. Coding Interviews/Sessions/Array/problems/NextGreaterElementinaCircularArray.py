"""
A circular array is one where the next element of the last element is the first element.

You know how standard arrays look. Instead of [1, 2, 3, 4], imagine the following, where after index 7, we'd move back to index 0.


Can you write a method nextLargerNumber(nums: array) to print the next immediate larger number for every element in the array?

Note: for any element within the circular array, the next immediate larger number could be found circularly-- past the end and before it. If there is no number greater, return -1.

Take the following example, with an analysis for each index:

JAVASCRIPT
nextLargerNumber([3, 1, 3, 4])
// [4, 3, 4, -1]
// 3's next greater is 4
// 1's next greater is 3
// 3's next greater is 4 again
// 4 will look to the beginning, but find nothing, so -1
Constraints
Length of the array <= 100000
The array will contain values between -1000000000 and 1000000000
Expected time complexity : O(n)
Expected space complexity : O(n)
"""

def next_larger_number(nums):
    result = [0] * len(nums)  # result array
    """
    stack to store the elements which
    are smaller than current element
    """
    stack = []

    top = 0  # initialize the stack element
    next_el = 0  # initialize the nums element

    stack.append(nums[0])  # push the first element in stack

    for i in range(1, len(nums)):  # loop from first element
        next_el = nums[i]  # current element
        if len(stack) > 0:
            top = stack.pop()  # get the top most element

            # if current element is greater than current, push to result
            while next_el > top:
                # we've found the next greater!
                result[nums.index(top)] = next_el

                if len(stack) == 0:
                    break
                top = stack.pop()

            # if top is greater than next_el then push back
            if top > next_el:
                stack.append(top)

        """
        push next_el back to stack so that
        we can find next element greater than it
        """
        stack.append(next_el)

    while len(stack) != 0:  # if no element is greater then push -1
        top = stack.pop()
        result[nums.index(top)] = -1

    return result

nums = [4,1,2,3]
print(next_larger_number(nums))