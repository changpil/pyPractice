import pprint

"get 7 digit telephone number and print all possible words"

data={"1":"1","2":["A","B", "C"],"3":["D","E","F"], "4":["G","H","I"],"5":["J","K","L"],"6":["M","N","O"],"7":["P","Q","R"], "8":["T","U","V"], "9":["W","X","Y"],"0":"0" }

#O(n*3*3^n)=O(n*3^n)
def get_all_words(phone_number, result):
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
    return result

phone="1234"
result={}

get_all_words(phone, result)

pprint.pprint(result[3])


