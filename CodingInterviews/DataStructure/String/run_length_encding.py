"""
Assume there is digits in word for encloding.

encoding
aaaabcccaa -> 4a1b3c2a

decoding
4a1b3c2a --> aaaabcccaa
"""


def encode(word):

    encoded =""
    ch = word[0]
    count = 1

    for i in range(1, len(word)):
        if ch != word[i]:
            encoded += str(count) + ch
            ch = word[i]
            count = 1
        else:
            count += 1
    encoded += str(count) + ch    #Error : Missed this line :, omitted last characters
    return encoded

def decode(word):

    decoded=""

    i = 0
    while i < len(word):
        j = i +1
        while word[j].isdigit():
            j += 1

        for _ in range(int(word[i:j])):
            decoded += word[j]

        i = j+1
    return decoded


print(encode("aaaffffsadddcc"))
print(decode("1a1c"))