# Given a set of distinct numbers, find all of its permutations.
#
# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:
#
# {1, 2, 3}
# {1, 3, 2}
# {2, 1, 3}
# {2, 3, 1}
# {3, 1, 2}
# {3, 2, 1}

def find_permutations_recursive(nums):
  result = []
  visited = set()
  runningResult = []
  helper(nums, len(nums) -1 , result, runningResult, visited)

  return result

def helper( nums, i, result, runningResult, visited):
    if i < 0:
        result.append(runningResult.copy())
        return

    for e in nums:
        if e not in visited:
            runningResult.append(e)
            visited.add(e)
            helper(nums, i -1, result, runningResult, visited)
            runningResult.pop()
            visited.remove(e)
from collections import deque
def find_permutations(nums):
    result = deque()
    result.append([nums[0]])
    for num in range(1, len(nums)):
        for i in range(len(result)):
            runningResult = result.popleft()
            for index in range(len(runningResult) + 1):
                tmp = runningResult[:index] + [nums[num]] + runningResult[index:]
                result.append(tmp.copy())
    return list(result)

def main():
  print("Here are all the permutations: " + str(find_permutations_recursive([1, 3, 5])))
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()