"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

"""

#O(N^2)
import collections
def minMeetingRooms(intervals):
    intervals.sort()
    i = 0
    while i < len(intervals):
        start, end = intervals[i][0], intervals[i][1]
        j = i + 1
        while j < len(intervals):
            s, e = intervals[j][0], intervals[j][1]
            if s < end:
                j += 1
            else:
                intervals.pop(j)
                intervals[i][1] = e
                end = e
        i += 1
    return len(intervals)

intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals)) # 2

intervals = [[7,10],[2,4]]
print(minMeetingRooms(intervals)) # 1

intervals = [[9,10],[4,9],[4,17]]
print(minMeetingRooms(intervals))  # 2


intervals = [[1,5],[8,9],[8,9]]
print(minMeetingRooms(intervals)) # 2