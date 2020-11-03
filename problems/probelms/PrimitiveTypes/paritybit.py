
"""
Date: 1/17/2018
Result: need sharpness
inout: 64 bits
output: charity bit (true or false)
"""
def print2Bytes(bits):
    binary=[]
    for i in range(16):
        bit = (bits & 1 )  # (bits8 |  0) does not work because other bits will follow.
        bits = bits >> 1
        if bit:
            binary.insert(0,"1")
        else:
            binary.insert(0,"0")
    print("".join(binary))


def get_charitybit(words):
    rv=0
    while words: # Error1:  used "len" instead of range
        print2Bytes(words)
        rv ^=(words & 1)
        words = words >> 1

    return rv

#print(get_charitybit(28))



