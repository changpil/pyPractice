# Average of Numbers

# Input
# _list = [10, 2, 3, 4, 8, 0]
# currentIndex = 0

# Output
# 4.5

def average(_list, currentIndex=0):
    if not _list:
        return None

    if currentIndex == len(_list):
        return 0

    _sum = _list[currentIndex] + average(_list, currentIndex + 1)

    if currentIndex == 0:
        return _sum / len(_list)
    else:
        return _sum

l = [3, -2, 5, 7,8]
print(l, end = "")
print(average(l, 0))