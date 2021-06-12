"""
Charlie has a chocolate factory. All his chocolate are of different heights, and are arranged in increasing order of their
heights. Unfortunately, Charlie has lost the count of chocolates of a particular height 'h'. Help him find the counts of the number of chocolates with the height 'h'.

Examples:

    2,4,5,5,6,6,6,6,6,9,10,100000
    h = 6
    Ansewer: 5

    3, 45, 45, 67, 10000
    h = 45
    answer = 2
"""


def charliesFactory(h, choco):
    start, end = 0, len(choco) -1

    while start <= end:
        mid = (start + end)//2
        if choco[mid] >= h:
            end = mid - 1
        elif choco[mid] < h:
            start = mid + 1

    if start == len(choco):
        return 0
    if choco[start] != h:
        return 0
    count = 0
    while start < len(choco) and choco[start] == h:
        count += 1
        start += 1
    return count
ch = [2,4,5,6, 6, 6]
print(charliesFactory(6, ch))

ch = [2,4,5,5,6,6,6,6,6,9,10,100000]
print(charliesFactory(6, ch))

ch = [2,4,5,5,6,6,6,6,6,9,]
print(charliesFactory(10, ch))

ch = [2,4,5,5,6,6,6,6,6,9,]
print(charliesFactory(1, ch))

ch = [6,6,6,6,6]
print(charliesFactory(6, ch))