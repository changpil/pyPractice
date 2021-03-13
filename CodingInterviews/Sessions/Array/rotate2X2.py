"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""


def rotateImage(a):
    m = len(a)
    n = len(a[0])
    for i in range(m // 2):
        for j in range(n):
            a[i][j], a[m - 1 - i][j] = a[m - 1 - i][j], a[i][j]


    for i in range(m):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
def print2D(a):
    for l in a:
        print(l)

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

a =rotateImage(a)

print2D(a)
