class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
    if n < 0:
        return -1
    memo = [0]*(n+1)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n+1):
        result = 0
        for mid in range(1, i+1):
            left = mid -1
            right = i - mid
            if left == 0 or right == 0:
                result += memo[left] + memo[right]
            else:
                result += memo[left] + memo[right] - 1
        memo[i] = result
    print(memo)
    return memo[n]
def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))
  print("Total trees: " + str(count_trees(4)))

main()