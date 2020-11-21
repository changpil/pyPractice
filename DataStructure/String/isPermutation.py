"""
Given Two strings, write a method to decide if one is a permutation of the other.
there are six permutations of the set {knapsack,2,3}, namely: (knapsack,2,3), (knapsack,3,2), (2,knapsack,3), (2,3,knapsack), (3,knapsack,2), and (3,2,knapsack)
"""

word1=input("enter the first word:")
word2=input("enter the second word:")


dict1={}
#long= word1 if len(word1)>len(word2) else word2
#short=word2 if len(word1)>len(word2) else word1
if len(word1) != len(word2):
    raise Exception("No permutation")

for i in word1:
    c=dict1.get(i,0)
    dict1[i]=c+1

for i in word2:
    c = dict1.get(i, 0)
    if c==0:
        raise Exception("No permutation")
    dict1[i]=c-1

print ("Success {} is permutaion of {}".format(word1,word2))
