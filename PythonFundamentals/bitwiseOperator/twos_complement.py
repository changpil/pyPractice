def twoscomplement(n):
    re=""
    bits = n.bit_length()
    if n < 0:
        bits += 1
    for _ in range(bits):
        b = n & 1
        re = str(b) + re
        n = n >> 1
    print(re)
    return re


#Pyhton keep signing bit...
#This will lead infinte loop
#-0b1
#-0b1
def twoscomplement1(n):
    re=""
    while n:
        b = n & 1
        re = str(b) + re
        n = n >> 1
    print(re)

#twoscomplement(-11)
#twoscomplement1(-11)


def twos(bstr):
    b = int(bstr, 2)
    twos = ~b + 1

    b_len = twos.bit_length() + 1 if twos < 0 else  twos.bit_length() + 0
    print(bin(b))
    # print(bin(twos))
    print(b_len)
    str_repr = ""
    for _ in range(b_len):
        str_repr =  "1" + str_repr if twos & 1 else  "0" + str_repr
        twos = twos >> 1
        print(str_repr)
    return str_repr


print(twos("1100"))
