# Problem Statement #
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
#
# Example 1:
#
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
# one [1,5].
#
# Example 2:
#
# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
#
# Example 3:
#
# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

# This is a horrible program
# def merge(intervals):
#     merged = []
#     merged.append(Interval(intervals[0].start, intervals[0].end))
#     for e in intervals:
#         start, end = e.start, e.end
#         append = False
#         for j in range(len(merged)):
#             m_start, m_end = merged[j].start, merged[j].end
#             # Error: I missed the equal sign
#             if m_start < start <= m_end and end > m_end:
#                 merged[j].end = end
#                 break
#             # In order to escape , I need to have equal sign
#             elif start <= m_start and end >= m_end:
#                 merged[j].start = start
#                 merged[j].end =end
#                 break
#             # I missed equal sign
#             elif m_start <= end < m_end and start < m_start:
#                 merged[j].start = start
#                 break
#             # check for every merged interval that spans i.
#             elif m_end < start or end < m_start:
#                 append = True
#             elif start < m_start and end > m_end:
#                 break
#         if append:
#             merged.append(Interval(start,end))
#     return merged


# Sort(NlogN)
def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    a = intervals[0]
    start , end = a.start, a.end
    for i in range(1, len(intervals)):
        b = intervals[i]
        if b.start <= a.end:
            end = max(a.end, b.end)
        else:
            mergedIntervals.append(Interval(start, end))
            start = b.start
            end = b.end
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals

def main():

  print("Merged intervals: ", end='')
  l = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
  for i in l:
    i.print_interval()
  print()
  for i in merge(l):
    i.print_interval()
  print()
  for i in l:
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  l = [Interval(6, 7), Interval(2, 4), Interval(5, 9)]
  for i in l:
    i.print_interval()
  print()
  for i in merge(l):
    i.print_interval()
  print()
  for i in l:
    i.print_interval()
  print()


  print("Merged intervals: ", end='')
  l = [Interval(1, 4), Interval(2, 6), Interval(3, 5)]
  for i in l:
      i.print_interval()
  print()
  for i in merge(l):
    i.print_interval()
  print()
  for i in l:
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  l = [Interval(2, 4), Interval(6, 7), Interval(1, 2)]
  for i in l:
      i.print_interval()
  print()
  for i in merge(l):
    i.print_interval()
  print()
  for i in l:
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  l = [Interval(2, 4),Interval(1, 2)]
  for i in l:
      i.print_interval()
  print()
  for i in merge(l):
    i.print_interval()
  print()
  for i in l:
    i.print_interval()
  print()

main()