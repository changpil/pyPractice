# Given a set with distinct elements, find all of its distinct subsets.
#
# Example 1:
#
# Input: [1, 3]
# Output: [], [1], [3], [1,3]
# Example 2:
#
# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

# DFS
def find_subsets_recursive(nums):
  subsets = []
  runningsubsets = []
  helper(nums, 0, subsets, runningsubsets)
  return subsets

def helper(nums, i, subsets, runningsubsets):
    if i == len(nums):
        subsets.append(runningsubsets.copy())
        return

    helper(nums, i + 1, subsets, runningsubsets)

    runningsubsets.append(nums[i])
    helper(nums, i +1, subsets, runningsubsets)
    runningsubsets.pop()



def find_subsets(nums):
    subsets = []
    subsets.append([])
    for e in nums:
        for i in range(len(subsets)):
            ns = subsets[i].copy()
            ns.append(e)
            subsets.append(ns)
    return subsets

def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets_recursive([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets_recursive([1, 5, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()