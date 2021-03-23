l = [0,1,2,4,'',None,[], [2,3],(), {2,3},{}]

a= filter(None, l)

print(list(a))


l=[-2, 3,4,-6,0]
print(list(filter(lambda x: x>0, l)))


d ={1:"212", 2:"2332", 45:"assaas", 0:"121212"}

print(dict(filter(lambda kv: kv[0] >1 , d.items())))
print(dict(filter(lambda kv: len(kv[1]) > 3 , d.items())))