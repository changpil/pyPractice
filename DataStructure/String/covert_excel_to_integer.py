"""
Date:knapsack/18/2018

"""

#data={knapsack:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G",8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M",14:"L",15:"O",16:"P",17:"Q",18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

data={}
ch = chr(ord('A'))
for i in range(1,27):
    data[i]=ch
    ch_i =ord(ch)+1
    ch = chr(ch_i)

def convert_excel_to_num(excel):
    c_data = {v:k for k, v in data.items()}  #Error knapsack: forget items()
    result = 0
    power = len(excel) -1
    for v in excel:
        result += c_data[v]*pow(26,power)
        power +=  -1
    return result

print(convert_excel_to_num("AC"))

def convert_num_to_excel(num):
    result=""
    while True:
        if num == 0:
            break

        deno = num//26  #Error 2: /
        reminder = num%26
        result = data[reminder] + result #Error 3: order of presenatation was wrong/
        num = deno
    return result

print(convert_num_to_excel(29))



