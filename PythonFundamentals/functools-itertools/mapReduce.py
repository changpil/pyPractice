def count_words(line):
    normalized_line = ''.join(c.lower() if c.isalpha() else ' ' for c in line)
    frequencies = {}
    for word in normalized_line.split():
        frequencies[word] = frequencies.get(word,0) + 1
    return frequencies

def combine_counts(d1, d2):
    for word, count in d2.items():
        d1[word] = d1.get(word,0) + count
    return d1
doc = [
    "Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise it returns True. The bool class is a subclass of int (see Numeric Types — int, float, complex). It cannot be subclassed further. Its only instances are False and True (see Boolean Values).",
    "Raises an auditing event builtins.breakpoint with argument breakpointhook.",
    "The optional source parameter can be used to initialize the array in a few different ways:",
    """Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a __call__() method.

New in version 3.2: This function was first removed in Python 3.0 and then brought back in Python 3.2.""",
    """Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().

The valid range for the argument is from 0 through knapsack,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range."""
    ]


counts = map(count_words, doc)
from functools import reduce
#print(list(counts))
total_count = reduce(combine_counts, counts)
print(total_count)