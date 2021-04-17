"""
Given an infinite stream of characters, build a system that sends a signal whenever a matching stream of characters, based on an input is encountered.

Example :  ................ageok googlefrgsdgsdgbsdfgsfbs*alexa*sdgfsgvdfvdsavsdf.........
Input : alexa
output :  call signal() whenever alexa is encountered.
"""

"""
public interface IStream {
    char next();
    void signal();
}

public class IStreamImpl implements IStream {
    // Don't implement.
}

public class Solution {
}
"""

"""
Input : ....adcadcabc....
             |    |
1. adcabc  
"""


def signal():
    print("Signal received")


import collections


def matchingString(stream, s):
    window = collections.deque()
    i = 0

    while i < len(s):
        window.append(stream.next())
        i += 1

    while True:
        if isSame(list(window), s):
            stream.signal()
        if window:
            window.popleft()
        window.append(stream.next())


def isSame(s1, s2):
    return "".join(s1) == s2


class Istream:
    def __init__(self, input):
        self.input = input
        self.p = 0

    def next(self):
        ch = self.input[self.p]
        self.p += 1
        return ch

    def signal(self):
        print("matching signal")


# stream = Istream("aaaaaaa")
# matchingString(stream, "a")


# stream = Istream(None)
# matchingString(stream, "a")

# stream = Istream("")
# matchingString(stream, "a")

# stream = Istream("................ageok googlefrgsdgsdgbsdfgsfbs*alexa*sdgfsgvdfvdsavsdf.........")
# matchingString(stream, "alexa")

# "alexalexa"

stream = Istream("alexalexa")
matchingString(stream, "alexa")
