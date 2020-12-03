def find_all_well_formed_brackets(n):
    result = []
    helper(n, 0, 0, result, "")
    return result


def helper(n, i, opened, result, tmp):
    if 2 * n == i:
        if opened == 0:
            result.append(tmp)
        return

    if opened < n:
        helper(n, i + 1, opened + 1, result, tmp + "(")

    if opened > 0:
        helper(n, i + 1, opened - 1, result, tmp + ")")
