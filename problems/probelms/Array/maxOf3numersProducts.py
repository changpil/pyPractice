"""
A unsorted array of integers is given; you need to find the max product formed my multiplying three numbers.
"""
import queue
def twos(fun=max,l=[]):
    tmp = l[:]
    max1 = fun(tmp)
    del tmp[tmp.index(max1)]
    max2 = fun(tmp)
    return max1, max2

def maxProductsOfthree(nums):
    if len(nums) < 3:
        raise ValueError
    if len(nums) == 3:
        return nums[0]*nums[1]*nums[2]

    p = list()
    q = list()
    r = list()

    for i in nums:
        if i > 0:
            if len(p) >= 3 and min(p) < i:
                del p[p.index(min(p))]
                p.append(i)
            if len(p) < 3:
                p.append(i)
        if i <= 0:
            if len(q) < 3:
                q.append(i)
            if len(r) < 3:
                r.append(i)
            if len(q) >= 3 and max(q) > i:
                del q[q.index(max(q))]
                q.append(i)
            if len(r) >= 3 and min(r) < i:
                del r[r.index(min(r))]
                r.append(i)



    print(p)
    print(q)
    print(r)
    possible_products=[]

    try:
        possible_products.append(p[0] * p[1] * p[2])
    except:
        pass

    try:
        possible_products.append(r[0] * r[1] * r[2])
    except:
        pass



    try:
        a1, a2 = twos(min, q)
        a3 = max(p)
        print(a1, a2, a3)
        possible_products.append(a1*a2*a3)
    except:
        pass


    try:
        a1, a2 = twos(max, r)
        a3 = min(p)
        possible_products.append(a1 * a2 * a3)
    except:
        pass

    print(possible_products)
    return max(possible_products)

nums=[1,0,-2,-3,-4,-5,-6, -7]
print(maxProductsOfthree(nums))