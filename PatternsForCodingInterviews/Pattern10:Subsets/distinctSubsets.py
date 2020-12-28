# Given a set of numbers that might contain duplicates, find all of its distinct subsets.
#
# Example 1:
#
# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]
# Example 2:
#
# Input: [1, 5, 3, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]


def find_subsets_recursive(nums):
  subsets = []
  runningsubsets = []
  visited = set()
  helper(nums, 0, subsets, runningsubsets, visited)
  return subsets

def helper(nums, i, subsets, runningsubsets, visited):
    if i == len(nums):
        t = tuple(runningsubsets)
        if t not in visited:
            subsets.append(runningsubsets.copy())
            visited.add(t)
        return

    helper(nums, i + 1, subsets, runningsubsets, visited)
    runningsubsets.append(nums[i])
    helper(nums, i +1, subsets, runningsubsets, visited)
    runningsubsets.pop()


def find_subsets(nums):
    subsets = []
    subsets.append([])
    nums.sort()
    previousset = []
    for i in range(len(nums)):
        if i >= 1  and nums[i] == nums[i-1]:
            for e in range(len(previousset)):
                previousset[e].append(nums[i])
                ns = previousset[e].copy()
                subsets.append(ns)

        else:
            previousset.clear()

            for e in range(len(subsets)):
                ns = subsets[e].copy()
                ns.append(nums[i])
                subsets.append(ns)
                previousset.append(ns.copy())

    return subsets

def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets_recursive([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets_recursive([1, 5, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets_recursive([1, 5, 3, 3, 3])))

main()