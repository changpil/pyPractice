def singleNonDuplicate(nums):
    # |even Index, odd Index, ..., Even Index, ....odd Index, Even Index
    # | 1, 1, 2, 3 , 3, 4, 4 |

    start, end = 0, len(nums) - 1

    if len(nums) == 1 or nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]

    while start <= end:
        mid = (start + end) // 2

        if nums[mid-1] != nums[mid] != nums[mid+1]:
            return nums[mid]
        elif (mid % 2 == 0 and nums[mid + 1] == nums[mid]) or (mid % 2 == 1 and nums[mid - 1] == nums[mid]):
            start = mid + 1
        else:
            end = mid - 1

a = [1,1,2,3,3,4,4,8,8]

print(singleNonDuplicate(a))