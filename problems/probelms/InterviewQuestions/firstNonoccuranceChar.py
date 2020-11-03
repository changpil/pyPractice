"""
"sasas sasdas tsasad " => t
"""


def nonoccuranceChar(s):
    data = [0]*126
    for i in s:
        data[ord(i)] = data[ord(i)] +1

    for i in s:
        if data[ord(i)] == 1:
            return i

    return -1

s = "hhello Tgood morning"
print(nonoccuranceChar(s))