def largest_product(_list):
    products = [[ 1 for _ in range(len(_list) + 1)] for _ in range(2)]
    print("{0: <{width}}".format(" ", width=6), end=" ")
    for i in _list:
        print("{0: <{width}}".format(i, width=6), end=" ")
    print()
    for i , num in enumerate(_list):
        products[0][i+1] = max(products[0][i]*num, products[1][i]*num,products[0][i])
        products[1][i+1] = min(products[0][i]*num, products[1][i]*num, products[1][i])
    for row in products:
        for e in row:
            print("{0: <{width}}".format(e, width=6), end=" ")
        print()
    return products[0][len(_list)]

a = [ 2, -3, 4, 4, 6, 7, -7, 8]

print(largest_product(a))

"""
Maximum Product Subarray
"""
def maximum_product_of_subarray(_list):

    max=0
    i_p, j_p = 0, 0

    for i in range(1, len(_list)):
        submax = 0
        sub_i_p, sub_j_p = 0, 0
        """
        First implementation was wrong:
        multiply one forst and last.
        for j in range(i-Pattern1:knapsack,-Pattern1:knapsack,-Pattern1:knapsack ):
            if submax < _list[i]*_list[j]:
                submax =  _list[i]*_list[j]
                sub_i_p, sub_j_p = i, j
        """
        for j in range(i-1,-1,-1 ):
            product_from_i_to_j = 1
            for m in range(j, i+1):
                product_from_i_to_j *= _list[m]
            if submax < product_from_i_to_j:
                submax =  product_from_i_to_j
                sub_i_p, sub_j_p = i, j

        if max < submax:
            max = submax
            i_p, j_p = sub_i_p, sub_j_p

    return (j_p, i_p)

print(maximum_product_of_subarray(a))


"""
Largest product  that can be made using n-Pattern1:knapsack entries
"""


def largest_product_using_n_1_entries(_list):

    max_product = 0
    for i in range(len(_list)):
        products = 1
        for j in range(len(_list)):
           if j !=i:
               products *=_list[j]
        max_product = max(max_product, products)
    return max_product

print(largest_product_using_n_1_entries(a))

