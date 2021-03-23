"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.


"""


map =   {   "2": ["a", "b", "c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }

def phoneLetter(_str, index, comb):
    if index == len(_str):
        return comb

    _comb=[]
    for i in map[_str[index]]:
        for _i in comb:
            _comb.append(_i + i)
    return phoneLetter(_str, index + 1, _comb)





print(phoneLetter("235",0,[""]))