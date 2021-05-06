# Minimum Meeting Rooms (hard) #
# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
#
# Example 1:
#
# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
# occur in any of the two rooms later.
# Example 2:
#
# Meetings: [[6,7], [2,4], [8,12]]
# Output: 1
# Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
# Example 3:
#
# Meetings: [[1,4], [2,3], [3,6]]
# Output:2
# Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
# hold all the meetings.
#
# Example 4:
#
# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
#
# Here is a visual representation of Example 4:

import math
from heapq import *
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end

# Wrong Problem-solving
# def isOverlapped(a, b):
#     if (a.start< b.start < a.end) or (a.start < b.end < a.end):
#         return True
#     if (b.start< a.end < b.end):
#         return True
#     if (a.start< b.start < b.end < a.end):
#         return True
#     return False
#
# def min_meeting_rooms(meetings):
#     meetings.sort(key= lambda x: (x.start, x.end))
#     return helper(meetings, 0)
#
# def helper(meetings, i):
#     if i == len(meetings):
#         return 0
#     a = meetings[i]
#     minRoom = 1 if i == len(meetings) -1 else math.inf
#     room =0
#     for n in range( i+1, len(meetings)):
#         meetings[i+1], meetings[n] = meetings[n], meetings[i+1]
#         b = meetings[i+1]
#         if isOverlapped(a, b):
#             room = 1
#         re = room + helper(meetings, i+1)
#         minRoom = min(minRoom, re )
#         meetings[i + 1], meetings[n] = meetings[n], meetings[i + 1]
#     return minRoom

def min_meeting_rooms(meetings):
  # sort the meetings by start time
  meetings.sort(key=lambda x: x.start)

  minRooms = 0
  minHeap = []
  for meeting in meetings:
    # remove all the meetings that have ended
    while(len(minHeap) > 0 and meeting.start >= minHeap[0].end):
      heappop(minHeap)
    # add the current meeting into min_heap
    heappush(minHeap, meeting)
    # all active meetings are in the min_heap, so we need rooms for all of them.
    minRooms = max(minRooms, len(minHeap))
  return minRooms

def main():


  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


  s = """
  Answer
  Minimum meeting rooms required: 2
  Minimum meeting rooms required: 2
  Minimum meeting rooms required: 1
  Minimum meeting rooms required: 2
  Minimum meeting rooms required: 2
  """
  print(s)
main()