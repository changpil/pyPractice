"""
Array Product
Given an array of numbers nums of size n, find an array of numbers products of size n, such that products[i] is the product of all numbers nums[j], where j != i.
Example One
Input:
5
1
2
3
4
5
Output:
120
60
40
30
24

Resultant Product array products = [products[0], products[1], products[2], products[3], products[4]]
= [(nums[1]*nums[2]*nums[3]*nums[4]), (nums[0]*nums[2]*nums[3]*nums[4]), (nums[0]*nums[1]*nums[3]*nums[4]), (nums[0]*nums[1]*nums[2]*nums[4]), (nums[0]*nums[1]*nums[2]*nums[3])]
= [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)]
= [120, 60, 40, 30, 24]

Example Two
Input:
3
4
9
10

Output:
90
40
36

Resultant Product array products = [products[0], products[1], products[2]]
= [(nums[1]*nums[2]), (nums[0]*nums[2]), (nums[0]*nums[1])]
= [(9*10), (4*10), (4*9)]
 = [90, 40, 36]

Notes

Input Parameters: There is only one argument: nums, denoting input array.
Output: Return an array of numbers products, denoting the required product array where products[i] is the (product of all numbers nums[j]) % (10^9 + 7), where j != i.

Constraints:

You can't use division anywhere in solution.
2 <= n <= 100000
-10^9 <= nums[i] <= 10^9, i = 0, 1, 2, … , n-1
products[i] >=0, i = 0, 1, 2, ... , n-1
You are allowed to use only constant extra space and the resultant product array will not be considered extra space.

Usage of resultant products array will not be considered as extra space used. Without using division is the key constraint to remember.
"""

def getProductArray(nums):
    products = [1]*len(nums)
    product = 1
    for i in range(1, len(nums)):
        product = product*nums[i-1]
        products[i] = product
    product = 1
    for i in range(len(nums)-2, -1, -1):
        product *= nums[i+1]
        products[i] = products[i] * product
    return products

nums= [4, 9, 10] # 90, 40, 36
print(getProductArray(nums))
nums= [1000000000, 1000000000]
print(getProductArray(nums))
nums= [-1000000000, -1000000000]
print(getProductArray(nums))
nums= [-100, 0]
print(getProductArray(nums))