# Similar Problems #
# Problem 1: Given a set of intervals, find out if any two intervals overlap.
#
# Example:
#
# Intervals: [[1,4], [2,5], [7,9]]
# Output: true
# Explanation: Intervals [1,4] and [2,5] overlap

def isOverlapped(intervals):
    if len(intervals) < 2:
        return False
    intervals.sort(key=lambda x: (x.start, x.end))

    a = intervals[0]
    start, end = a.start, a.end

    for i in range(1, len(intervals)):
        b = intervals[i]
        if b.start <= a.end:
            return True
        else:
            start = b.start
            end = b.end
    return False

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

print("Overlapped intervals: ", end='')
l = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
for i in l:
    i.print_interval()
print()
print(isOverlapped(l))


print("Overlapped intervals: ", end='')
l = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
for i in l:
    i.print_interval()
print()
print(isOverlapped(l))


print("Overlapped intervals: ", end='')
l = [Interval(1, 4), Interval(2, 6), Interval(3, 5)]
for i in l:
    i.print_interval()
print()
print(isOverlapped(l))



print("Overlapped intervals: ", end='')
l = [Interval(2, 4),Interval(1, 2)]
for i in l:
    i.print_interval()
print()
print(isOverlapped(l))