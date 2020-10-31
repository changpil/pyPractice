def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

s = "hello my name is Chang. HOw are you? it seems ok fo rnow"
sorted_s = sort_by_last_letter(s.split())
print(sorted_s)