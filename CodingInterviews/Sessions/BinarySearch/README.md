# Binary Search Variants

### Template
```
start, end = 0, len(nums) - 1   
while start <= end:  
    mid = (start + end)//2   
    if nums[mid] == target:   
        return mid
    elif nums[mid] lies in the left zone:
        start = mid + 1
    else:
        end = mid - 1
   
    AT this point, the end | start boundry demarcates the left and the right zone      
```

### Session 1   
##### 704. Binary Search (easy)   
##### 374. Guess Number High or Lower (easy)   
##### 278.First Bad Version (easy)   
##### 35. Search Insert Position (easy)
##### 744. Find Smallest Letter Greater Than Target (easy)
##### 34. Find First Last Position of Element in Sorted Array (Medium)
##### 1150. Check if a Number is Majority Element in a Sorted Array (easy)
##### 74. Search a 2D Matrix (medium)
##### 702. Search in a Sorted Array of Unknown Size (medium)
##### 1064. Fixed Point (easy)
##### 540. Single Element in a Sorted Array ( medium)
##### 1228. Missing Number in arithmetic Progression (easy)
##### 1060. Missing Element in Sorted Arary (medium)
### Session 2
##### 941. Valid Mountain Array (easy)
##### 852. Peak Index in a Mountain Array (easy) 
##### 1095. Find in a Mountain Array (hard)
##### 162. Find Peak Element (medium)
##### 153. Find Minimum in Rotated Sorted Array (medium)
##### 154. Find Minimum in Rotated Sorted Array II (hard)
##### 33. Search In Rotated Sorted Array (medium)
##### 81. Search in Rotated Sorted Array II ( medium)
