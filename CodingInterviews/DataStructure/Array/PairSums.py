# O(n^2)
def numberOfWaysN2(arr, k):
  arr.sort()
  i, j = 0, len(arr)-1
  out = 0
  while j >= 0:
    cur = arr[j]
    target = k - cur
    i = 0
    while i < j:
      if arr[i] == target:
        out += 1
      elif arr[i] > target:
        break
      i += 1
    j -= 1
  return out

# O(N)
import collections
def numberOfWays(arr, k):
    result = 0
    vi = collections.defaultdict(set)
    for i, v in enumerate(arr):
        vi[v].add(i)
    for i, v in enumerate(arr):
        target = k - v
        if target in vi:
            indexes = vi[target]
            if i in indexes:
                result += len(indexes) -1
            else:
                result += len(indexes)

    return result//2









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  print(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  print(expected_2, output_2)