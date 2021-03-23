def isMajorityElement(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    if start == len(nums) or nums[start] != target:
        return False
    leftmost = start
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    rightmost = end
    print(leftmost, " ", rightmost)
    if rightmost - leftmost + 1 > len(nums) // 2:
        return True
    return False


nums =[2,4,5,5,5,5,5,6,6]
t = 5

print(isMajorityElement(nums, t))


nums =[438885258,438885258]
t = 438885258
print(isMajorityElement(nums, t))

# nums = [17254032,44726461,94429656,95088006,110536255,138190931,150275052,164761538,221923321,296618557,305947091,332191050,372173382,381735837,396788118,429860682,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,437749703,455951973,463237207,498375239,526236757,537304401,621610945,658169340,678150935,718727426,744118395,763870453,793588980,991511570]
# t = 437749703
nums = [2,4,5,5,5,5,5,5, 6,6,6]
t = 5
print(len(nums))
print(isMajorityElement(nums, t))