import hashlib
# 128 bits

def printb(b):
    for _ in range(8):
        print(b & 1, end = "")
        b >>= 1
    print()

def getbyte(b ):
    abyte = 0
    for i in range(8):
        abyte += (b & 1 << i)
    return abyte

def main():
    bytea = hashlib.md5('http://stackoverflow.com212121'.encode()).digest()
    num = 0
    for b in bytea:
        num <<= 8
        num |= b
    for i in range(16):
        printb(num)
        num >>= 8
main()