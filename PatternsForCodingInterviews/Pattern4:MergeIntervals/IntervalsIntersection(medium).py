# Problem Statement #
# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
#
# Example 1:
#
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:
#
# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.
# #

# Not working : Collectness
# def check(a, b):
#     start , end = 0, 1
#     result = -1
#     if a[end] < b[start]:
#         result = 1
#     elif a[start]> b[start and b[start] <= b[end]]:
#         result = 2
#     elif a[start] <= b[start] <= b[end] <= a[end]:
#         result = 3
#     elif b[start] <= a[start] <= a[end] <= b[end]:
#         result = 4
#     elif b[start] < a[start] and a[start] <=b[end] <= a[end]:
#         result = 5
#     else:
#         result = 6
#
#     return result
#
#
# def intervalIntersection(interval_a, interval_b):
#     i , j = 0,0
#     start, end = 0, 1
#     intersection = []
#
#     while i <len(interval_a) and j < len(interval_b):
#         a = interval_a[i]
#         b = interval_b[j]
#         type = check(a, b)
#
#         if type == 1:
#             i += 1
#         elif type == 2:
#             intersection.append([b[start], a[end]])
#             i += 1; j += 1
#         elif type ==3 or type ==4:
#             intersection.append( [ max(a[start], b[start]) , min(a[end], b[end]) ])
#             i += 1; j += 1
#         elif type ==5:
#             intersection.append([a[start],b[end]])
#             i += 1; j += 1
#         elif type == 6:
#             j += 1
#
#     return intersection

# def main():
#   print("Intervals Intersection: " + str(intervalIntersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
#   print("Intervals Intersection: " + str(intervalIntersection([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

def check(a, b):
    start , end = 0, 1
    result = -1
    if a[end] < b[start]:
        result = 1
    elif a[start] < b[start] and b[start] <= a[end] <= b[end]:
        result = 2
    elif a[start] <= b[start] <= b[end] <= a[end]:
        result = 3
    elif b[start] <= a[start] <= a[end] <= b[end]:
        result = 4
    elif b[start] < a[start] and a[start] <= b[end] <= a[end]:
        result = 5
    else:
        result = 6

    return result


def intervalIntersection(interval_a, interval_b):
    i , j = 0,0
    start, end = 0, 1
    intersection = []

    while i <len(interval_a) and j < len(interval_b):
        a = interval_a[i]
        b = interval_b[j]
        type = check(a, b)

        if type == 1:
            i += 1
        elif type == 2:
            intersection.append([b[start], a[end]])
            i += 1
        elif type ==3:
            intersection.append( [ max(a[start], b[start]) , min(a[end], b[end]) ])
            j += 1
        elif type ==4:
            intersection.append( [ max(a[start], b[start]) , min(a[end], b[end]) ])
            i += 1
        elif type ==5:
            intersection.append([a[start],b[end]])
            j += 1
        elif type == 6:
            j += 1

    return intersection

def main():
  print("Intervals Intersection: " + str(intervalIntersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(intervalIntersection([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

main()
