"""
Given a list of reserved seats on a plane, find the number of three-person families you can fit together in the unreserved seats.
"""
import collections
def solution(rows, S):
    reservedSeats = collections.defaultdict(lambda: set())
    for seat in S.split():
        row, col = seat[:-1], seat[-1]
        reservedSeats[int(row)].add(col)

    NumOfFamilyAvailability = 3*rows

    for i in range(1, rows + 1):
        occupiedCols = reservedSeats[i]
        if 'A' in occupiedCols or 'B' in occupiedCols or 'C' in occupiedCols:
            NumOfFamilyAvailability -= 1
        elif 'H' in occupiedCols or 'J' in occupiedCols or 'K' in occupiedCols:
            NumOfFamilyAvailability -= 1
        elif ('D' in occupiedCols and 'G' in occupiedCols) or 'E' in occupiedCols or 'F' in occupiedCols:
            NumOfFamilyAvailability -= 1
    return NumOfFamilyAvailability

S = "1A 3C 2B 4G 5A"
print(solution(5, S)) # 11
S= "1A 2F 1C"
print(solution(2, S)) # 4

S= "1A 2D 1C"
print(solution(2, S)) # 5

S= "1A 2D 2G 1C"
print(solution(2, S)) # 4


S= "1A 2D  1J"
print(solution(2, S)) # 4


S= ""
print(solution(2, S)) # 4

