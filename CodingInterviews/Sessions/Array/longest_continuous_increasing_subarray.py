

def longest_continuous_increasing_subarray(_list):
    max_subarray=0
    i_p = 0
    j_p = 0

    for i in range(len(_list)):
        max_in_i = 0
        sub_i_p = i
        sub_j_p = i
        for j in range(i+1, len(_list)):
            if _list[sub_i_p] < _list[j]:
                max_in_i += 1
                sub_i_p += 1
                sub_j_p = j
            else:
                break
        if max_subarray < max_in_i:
            max_subarray = max_in_i
            i_p = i
            j_p = sub_j_p

    return (i_p, j_p)

a=[2,3,4,-4, -2, 3, 4, 7, 3, 4]
a = [0, -1, -2]
print(longest_continuous_increasing_subarray(a))
