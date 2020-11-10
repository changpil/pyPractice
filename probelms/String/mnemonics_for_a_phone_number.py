"""
"get 7 digit telephone number and print all possible words"

data={"1":"1","2":["A","B", "C"],"3":["D","E","F"], "4":["G","H","I"],"5":["J","K","L"],"6":["M","N","O"],"7":["P","Q","R"], "8":["T","U","V"], "9":["W","X","Y"],"0":"0" }

"""



data={"1":"1",
      "2":["A","B", "C"],
      "3":["D","E","F"],
      "4":["G","H","I"],
      "5":["J","K","L"],
      "6":["M","N","O"],
      "7":["P","Q","R"],
      "8":["T","U","V"],
      "9":["W","X","Y","Z"],
      "0":"0" }

#O(n*3*3^n)=O(n*4^n)
def get_all_words(phone_number, result=None):
    if result == None:
        result = {}
    for i, c in enumerate(phone_number):
        for j in data[c]:
            if i == 0:
                w1 = result.get(1,[])
                w1.append(j)
                result[0] = w1
            else:
                sub_result= result.get(i-1, [])
                new_result= result.get(i,[])
                for sub_word in sub_result:
                       new_result.append(sub_word+j)
                result[i]=new_result
    return result[len(phone_number)-1]
print(get_all_words("1234"))

memonics={1:"1",
        2:["A","B", "C"],
        3:["D","E","F"],
        4:["G","H","I"],
        5:["J","K","L"],
        6:["M","N","O"],
        7:["P","Q","R"],
        8:["T","U","V"],
        9:["W","X","Y", "Z"],
        0:"0" }

#O(n4^N)
def get_all_mnemonics(digits):
    results =[]
    if digits < 10:
        for c in memonics[digits]:
            results.append(c)
        return results

    sub_lists = get_all_mnemonics(digits//10)
    c = digits%10
    for sub_list in sub_lists:
        for m in memonics[c]:
            results.append(sub_list + m)

    return results

print(get_all_mnemonics(1234))