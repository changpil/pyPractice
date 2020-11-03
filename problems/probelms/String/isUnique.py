"""
Implement an algorithm to determin if a string has all unique charachters.
  space is included? Small and Capital?
what if you cannot use additional data structure?
"""

#This include every characters
def dup1():
    word = input("any word for checking duplicated characters?")
    set_word=set(word)
    print(set_word)
    if len(word) != len(set_word):
        raise Exception("There are duplicate characters")
    print("There is no duplicated charcters")

#This include every characters except space and newline
def dup2():
    word = input("any word for checking duplicated characters (Except space and newline)?")
    word=word.strip(' \n\t')
    print(word)
    set_word = set(word)
    if len(word) != len(set_word):
        raise Exception("There are duplicate characters")
        print("There is no duplicated charcters")

    # This include every characters except space and newline
def dup3():
    word = input("any word for checking duplicated characters (Except space and newline)?")
    print(word)
    dict={}
    for i in word:
        count=dict.get(i,0)
        if count == 1:
            raise Exception("There are duplicate characters")
        dict[i]=count+1

    print("There is no duplicated charcters")

# without additional data structure?
def dup4():
    word = input("any word for checking duplicated characters?")
    array=[ 0 for i in range(0,ord('z'))]
    for i in word:
        array[ord(i)]+=1

    for i in array:
        if i > 1:
            raise Exception("There are duplicate characters")
    print ("There is no duplicated charcters")


##Python3
## chr(97) ==> a
## ord('z') ==> 112
dup3()

