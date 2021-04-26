"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0)
"""


def isRobotBounded(instructions):
    direction = "west"
    x, y = 0, 0
    for _ in range(4):
        for move in instructions:
            if move == "G" and direction == "west":
                x += 1
            elif move == "G" and direction == "east":
                x -= 1
            elif move == "G" and direction == "north":
                y += 1
            elif move == "G" and direction == "south":
                y -= 1
            elif move == "L" and direction == "west":
                direction = "north"
            elif move == "L" and direction == "east":
                direction = "south"
            elif move == "L" and direction == "north":
                direction = "east"
            elif move == "L" and direction == "south":
                direction = "west"
            elif move == "R" and direction == "west":
                direction = "south"
            elif move == "R" and direction == "east":
                direction = "north"
            elif move == "R" and direction == "north":
                direction = "west"
            elif move == "R" and direction == "south":
                direction = "east"
        if x == 0 and y == 0:
            return True

    return False


instructions = "GGLLGG"
print(isRobotBounded(instructions))

instructions = "GG"
print(isRobotBounded(instructions))