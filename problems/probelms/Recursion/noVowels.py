def noVowels(_str):
    if not _str:
        return True

    if _str[0] in "aeiou":
        return False

    return noVowels(_str[1:])

print(noVowels("hllttttdi"))
