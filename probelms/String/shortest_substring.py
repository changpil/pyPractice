"""
Given an input string "aabbccba", find the shortest substring from the alphabet "abc".
In the above example, there are these substrings "aabbc", "aabbcc", "ccba" and "cba". However the shortest substring that contains all the characters in the alphabet is "cba", so "cba" must be the output.

Output doesnt need to maintain the ordering as in the alphabet.

Other examples:
input = "abbcac", alphabet="abc" Output : shortest substring = "bca".

"""
def substring(w1, w2):
    w2_set=set(w2)
    result={}
    last=len(w1)
    for i in range(last):
        for j in range(i+1,last):
            sub_str=w1[i:j]
            print(sub_str)
            if w2_set.issubset(set(sub_str)):
                result[abs(i-j)]=(i,j)

    print(result)
    for i in sorted(result.keys()):
        return w1[result[i][0]:result[i][1]]
    return None

print( substring("aabbccba","abc" ))