print(list(map(lambda x: x*2, [0,1,2,3,4])))

a = ['name', 'python', 'points', 10,  'name', 'java', 'points', 8]

l =list(map(lambda x: str(x), a))
print(l)

d = {len(x):x for x in l}
print(d)

a=[1,2,3,4,5]
b=[True, False,True,False,True]

print(list(map(lambda a, b: {a:b} , a, b)))