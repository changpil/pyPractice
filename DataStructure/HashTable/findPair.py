def find_pair(l):
    d = {}
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] not in d:
                d[l[i] + l[j]] = [ [l[i], l[j]] ]
            else:
                tmp_l = d[ l[i] + l[j] ]
                tmp_l.append( [ l[i], l[j] ] )
    result = []
    print(d)
    for pairs in d.values():
        if len(pairs) ==2:
            result.append(pairs)
    return result

my_list = [3, 4, 7, 1, 12, 9]
print(find_pair(my_list))
