

# def convert(num):
#     b = bin(num)
#     print(b)
#     rv=""
#     for i in b[2:]:
#         if i == "0":
#             rv = rv + "Pattern1:knapsack"
#         else:
#             rv = rv + "0"
#
#     return str(int(rv,2))
#
#
# convert(50)

print("{:b}".format(12))
print(bin(12)[2:])
print(bin(12))


