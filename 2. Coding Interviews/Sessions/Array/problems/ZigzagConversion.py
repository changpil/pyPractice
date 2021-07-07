"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
"""

# This will fail wuth miidle rows.
import pprint

def zigzag_fail(str1, num):
    _str=str()
    _str+=str1[::num+num-2]
    i = 1
    while i < num-1:
        _str+=str1[i::num-i]
        i+=1
    _str+=str1[num-1::num+num-2]
    return _str

def zigzag(str1, num):
    try:
        kk=num-2
        base=[['' for j in range(len(str1))] for i in range(num)]
        k=0
        for i in range(len(str1)):
            if i%(num-1) == 0:
                for j in range(num):
                    base[j][i] = str1[k]
                    k += 1
            else:
                col= k%(num-1)
                base[kk][i] = str1[k]
                kk -= 1
                if kk == 0:
                    kk = num-2
                k+=1
    except:
        pass

    pprint.pprint(base)
    return base

def get_zigzag(a):
    _str=str()
    for i in range(len(a)):
        for j in range(len(a[0])):
            _str += a[i][j] if a[i][j] is not " " else ""
    return _str

cc= zigzag("PAYPALISHIRING", 5)
print(get_zigzag(cc))

def convert(s, numRows):
    if numRows == 1:
        return s
    result = [[] for _ in range(numRows)]
    span = numRows + numRows - 2
    for i in range(len(s)):
        n = i % span
        if n < numRows:
            result[n].append(s[i])
        else:
            result[span - n].append(s[i])

    return "".join(map("".join, result))

cc= zigzag("PAYPALISHIRING", 5)
print(get_zigzag(cc))