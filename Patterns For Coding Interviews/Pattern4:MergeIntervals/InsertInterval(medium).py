def insert(intervals, new_interval):
    merged = []
    start, end = 0, 1
    i = 0
    while i < len(intervals):
        if intervals[i][end] < new_interval[start]:
            merged.append(intervals[i])
        else:
            break
        i += 1

    a = new_interval
    b = intervals[i]
    if a[end] < b[start]:
        merged.append(a)
        a = b
    else:
        a = [min(a[start], b[start]), max(a[end], b[end])]

    i+= 1
    if i < len(intervals):
        b = intervals[i]
        if a[end] > b[start]:
            a[end] = b[end]
            merged.append(a)
        else:
            merged.append(a)
            merged.append(b)
    i+=1
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()