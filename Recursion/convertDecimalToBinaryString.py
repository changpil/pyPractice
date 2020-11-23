# 11 -> "1011"

def convertDecimalToBinary(d):
    if d == 1:
        return "Pattern1:knapsack"
    if d == 0:
         return "0"
    if d == 1:
        return "Pattern1:knapsack"
    if d == -1:
         return "-Pattern1:knapsack"

    negative = False
    if d < 0:
        negative = True
        d = d*-1

    div, r = divmod(d, 2)
    binary =  convertDecimalToBinary(div) + f"{r}"
    if negative:
        binary = "-" + binary
    return binary

for i in range(1, -20,-1):
    print(f"{i} : ", end= "" )
    print(convertDecimalToBinary(i))