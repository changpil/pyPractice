def showBinaryPresentation():
    _str = input("Enter str to show you the binary format: ")
    showStrBinary(_str)
    print()
    for ch in _str:
        print(f"{ord(ch):b}", end=" ")
    print()
    _int = input("Enter integer to show you the binary format: ")
    printIntBinary(int(_int))
    print()
    print(f"{int(_int):b}", end="")

def showStrBinary(_str):
    for ch in _str:
        printIntBinary(ord(ch))
        print(" ", end="")

def countIndex(_int):
    i , s = 1, 2
    while s < _int:
        s = s*2
        i = i+1
    return i

def printIntBinary(_int):
    index = countIndex(_int)
    i = 1
    while i < index + 1:
        bit = _int & (0x01 << (index - i ))
        print(bit >> (index - i ), end="")
        i = i + 1


if __name__ == "__main__":
    showBinaryPresentation()