# Generate All Subsets Of A Set

def generate_all_subsets(s):
    c = list()
    helper(s, len(s), c, "")
    return c

def helper(s, level, c, partial):
    # if s == "":
    #     return

    if level == 0:
        c.append(partial)
        return

    helper(s[1:], level - 1, c, partial)
    helper(s[1:], level - 1, c, partial + s[0])

print(generate_all_subsets("xy"))