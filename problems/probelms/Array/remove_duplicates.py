def remove_duplicates(_list):


    i = 0

    while i < len(_list):
        while _list.count(_list[i]) != 1:
            duplicated_index = _list.index(_list[i], i+1)
            del _list[duplicated_index]

        i += 1
    return _list

a =[1,2,1, 3,3, 5 , 1, 3]

print(remove_duplicates(a))
