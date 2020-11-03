"""
look-and-say sequence:
1, 11, 21, 1211,111221,312211,13112221, 1113213211, ....

Write a function that takes as input an integer n and return the nth integer in the look-and-say sequence
"""

def look_and_say_sequence(k):

    sequence = "1"

    for _ in range(k):
        new_sequence = ""
        i = 0
        while i < len(sequence):
            count = 1
            j = i + 1
            while j < len(sequence):
                if sequence[i] == sequence[j]:
                    count += 1
                    j += 1
                    i += 1
                else:
                    break
            new_sequence += str(count) + sequence[i]
            i += 1
        sequence = new_sequence
    return sequence


print(look_and_say_sequence(10))









