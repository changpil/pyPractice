def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    dic = dict()

    for e in nums1:
        arr = dic.get(e, [0, 0])
        arr[0]= arr[0] + 1
        dic[e] = arr

    for e in nums2:
        arr = dic.get(e, [0, 0])
        arr[1] = arr[1] + 1
        dic[e] = arr

    rv = []
    for k, v in dic.items():
        for i in range(min(v[0], v[1])):
            rv.append(k)
    return rv

a = [1,1]
b = []
print(intersect(a,b))