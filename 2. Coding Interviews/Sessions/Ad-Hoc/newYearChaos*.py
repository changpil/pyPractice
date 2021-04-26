"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
Example
If person  bribes person , the queue will look like this: . Only  bribe is required. Print 1.
Person  had to bribe  people to get to the current position. Print Too chaotic.
Function Description
Complete the function minimumBribes in the editor below.
minimumBribes has the following parameter(s):
int q[n]: the positions of the people after all bribes
Returns
No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
"""


# def minimumBribes(q):
#     minimumBribes = 0
#     i = 0
#     while i < len(q) -1:
#         targetValue = q[i]
#         targetIndex = targetValue -1
#         index = i
#         bribes = 0
#         while index <len(q) and index != targetIndex:
#             q[index], q[index+1] = q[index+1], q[index]
#             bribes += 1
#             index += 1
#             if bribes > 2:
#                 return "too chaotic"
#         minimumBribes += bribes
#         if q[i] == i + 1:
#             i += 1
#     return minimumBribes

def minimumBribes(q):
    valIndexMap = {}
    for i, v in enumerate(q):
        valIndexMap[v] = i
    minimumBribes = 0
    for value in range(len(q), 0, -1):
        index = valIndexMap[value]
        targetIndex = value -1
        bribes = 0
        while index < len(q) - 1 and index != targetIndex:
            q[index], q[index+1] = q[index+1], q[index]
            valIndexMap[q[index]] = index
            bribes += 1
            index += 1
            if bribes > 2:
                return "too chaotic"
        minimumBribes += bribes
    return minimumBribes
q = [2, 1, 5, 3, 4]
print(minimumBribes(q)) # 3

q = [2, 5, 1, 3, 4]
print(minimumBribes(q)) # too chaotic

q = [5, 1, 2, 3, 7, 8, 6, 4]
print(minimumBribes(q)) # too chaotic

q = [1,2, 5, 3, 7, 8, 6, 4]
print(minimumBribes(q)) # 7