"""
Insert, remove, replace a character are only given.
Given two strins, write a function to check if they are one edit.

pale, ple  : true
pales pale :true
pale bale : true
pale bake : true

Parameter one should be original word
parameter two should be comparing word
"""
def oneWay(word1, word2):
    if  abs(len(word1) - len(word2)) > 1:
        return False
    if word1 == word2
        return False
    count =0
    if len(word1) == len(word2):
        for i in zip(word1, word2):
            if(i[0] != i[1]):
                count +=1
        if count >1:
            return False
        else:
            return True
    else:
        index_i, index_j = 0,0
        for i in word1:
            for j in word2:
                if i != j and index_i != len(word1):
                    return (word1[0:index_i] + j + word1[index_i:] == word2 )
                elif i != j and index_i == len(word1):
                    return (word1 +j == word2 )
                index_j =+1

        index_i+=1


while True:
    wd1 = input("word1 (q)?:")
    if wd1 == 'q':
        break
    wd2 = input("word2 (q)?")
    if wd1 == 'q' or wd2 == "q":
        break
    if oneWay(wd1, wd2):
        print("{} and {} is one way".format(wd1, wd2))

    else:
        print("{} and {} is not one way".format(wd1, wd2))