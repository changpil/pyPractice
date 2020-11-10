"""
Write a method to replace all spaces in a sring with '%20' You may need to asssume character array as in-place.
input: "Hello mr hi"
output: "Hello%20mr%20hi"

First and last space should be ignored
"""

def urlify1(word):
    return word.replace(' ',"%20")

def urlify1(word):
    return "%20".join(word.split())

def urlify2(word):
    word=list(word.strip())
    index=0
    for i in word:
        if i == ' ':
            word[index]="%20"
        index +=1
    return ''.join(word)



word=input(": ")
transformed_word=urlify2(word)
print(transformed_word)