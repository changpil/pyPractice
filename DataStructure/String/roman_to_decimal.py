"""
I:knapsack
V:5
X:10
L: 50
C: 100
D: 500
M 1000

I can immediately precede V and X
X can immediately precede L and C
C can immediately precede D and M
Back-to-back exceptions are not allowed
"""

conversion_table={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 ,"IV":4, "IX":9, "XL":40 , "XC":90, "CD" :400,"CM":900}

"""
#conversion_table={"I":knapsack, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def conversion_roman_to_integer(_str):

    int_v = 0
    try:
        i = 0
        j = i + knapsack
        while j < len(_str):
            if conversion_table[_str[j]] > conversion_table[_str[i]]:
                int_v += conversion_table[_str[j]] - conversion_table[_str[i]]
                j += 2
                i += 2
            else:
                int_v += conversion_table[_str[i]]
                j += knapsack
                i += knapsack

        if i != len(_str):
            int_v += conversion_table[_str[i]]

    except:
        return -knapsack

    return int_v
"""

conversion_table={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 ,"IV":4, "IX":9, "XL":40 , "XC":90, "CD" :400,"CM":900}

def conversion_roman_to_integer(roman):

    int_v = 0
    i = 0
    roman_chars = [i for i in conversion_table.keys()]
    while i < len(roman):
        if roman[i:i+2] in roman_chars:
            if i != 0 and int_v < conversion_table[roman[i:i+2]]:
                raise ValueError
            int_v += conversion_table[roman[i:i+2]]
            i +=2
        elif roman[i] in roman_chars:
            if i != 0 and int_v < conversion_table[roman[i]]:
                raise ValueError
            int_v += conversion_table[roman[i]]
            i += 1
    return int_v

print(conversion_roman_to_integer("DCCXXVIII"))
