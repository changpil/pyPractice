# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.
#
# To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].
#
# Example 1:
#
# Input: [
#   [1,0,1],
#   [1,1,1],
#   [0,1,1]
# ]
# Output: [
#   [0,1,0],
#   [0,0,0],
#   [0,0,1]
# ]
# Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]
#
# Example 2:
#
# Input: [
#   [1,1,0,0],
#   [1,0,0,1],
#   [0,1,1,1],
#   [1,0,1,0]
# ]
# Output: [
#   [1,1,0,0],
#   [0,1,1,0],
#   [0,0,0,1],
#   [1,0,1,0]
# ]


def flip_and_invert_image(matrix):
  tmp = [[ matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]

  for i in range(len(matrix)):
      for j in range(0, len(matrix)):
          matrix[i][j] = tmp[i][len(matrix[j]) -1 -j] ^ 1

  return matrix

# Inplace
def flip_and_invert_image_inplace(matrix):
  for i in range(len(matrix)):
      start, end  = 0, len(matrix) -1

      for j in range(0, (len(matrix)-1)//2 +1):
            jstart, jend  = start + j, end - j
            if jstart != jend:
                matrix[i][jstart], matrix[i][jend] = matrix[i][jend] ^ 1, matrix[i][jstart] ^ 1
            else:
                matrix[i][jstart] = matrix[i][jstart] ^ 1
  return matrix

def main():
  print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
  print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

  print(flip_and_invert_image_inplace([[1,0,1], [1,1,1], [0,1,1]]))
  print(flip_and_invert_image_inplace([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
main()
