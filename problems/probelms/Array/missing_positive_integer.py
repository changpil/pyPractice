def find_missing_integer(_list, mid = 0, expected_number =0):
    if len(_list) < 2:
       return -1

    if mid >= len(_list):
        if _list[mid-1] == expected_number -1:
            return _list[mid-1]+1
        else:
            return -1

    if mid == 0:
        mid  = len(_list)//2
        expected_number = _list[0]+ mid


    if _list[mid] == expected_number:
        mid = (mid + len(_list))//2  #Error : (mid + len(_list))//2
        expected_number = _list[0] + mid
        return find_missing_integer(_list, mid, expected_number)
    else:
        if _list[mid-1] == expected_number -1:
            return _list[mid-1]+1   #Error: mid
        else:
            mid = mid//2
            expected_number = _list[0] + mid
            return find_missing_integer(_list, mid, expected_number)
    return -1

a =[2,3,5]
print(find_missing_integer(a))