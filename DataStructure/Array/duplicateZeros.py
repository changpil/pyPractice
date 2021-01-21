# class Solution:
#     def duplicateZeros(self, arr):
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         lasti = len(arr) - 1
#         shift = 0
#         for i in arr:
#             if i == 0:
#                 shift += 1
#
#
#         while lasti >= 0:
#             shifti = lasti + shift
#             if shifti < len(arr):
#                 arr[shifti] = arr[lasti]
#                 if arr[lasti] == 0:
#                     shifti -= 1
#                     arr[shifti] = arr[lasti]
#                     shift -= 1
#             else:
#                 if arr[lasti] == 0:
#                     if shifti -1 < len(arr):
#                         shifti -= 1
#                         arr[shifti] = arr[lasti]
#                     shift -= 1
#             lasti -= 1


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        lasti = len(arr) - 1
        shift = 0
        for i in arr:
            if i == 0:
                shift += 1

        tmp = shift
        while tmp:
            arr.append(0)
            tmp -= 1
        tmp = shift
        for i in range(lasti, -1, -1):
            arr[i + shift] = arr[i]
            if arr[i] == 0:
                shift -= 1
                arr[i + shift] = arr[i]

            if shift == 0:
                break

        while tmp:
            arr.pop()
            tmp -= 1
# a = [1,0,2,3,0,4,5,0]
# Solution().duplicateZeros(a)
# print(a)

a = [8,4,5,0,0,0,0,7]
Solution().duplicateZeros(a)
print(a)