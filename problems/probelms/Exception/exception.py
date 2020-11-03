import sys
"""
try:
    pass
    raise Exception("sss")
except Exception as ex:
    print("except {}".format(sys.argv[1]))
"""

sum = [1,2,3, 4,5]
prod= [6,7,9, 10]

for i in zip(sum, prod):
    print(i)


