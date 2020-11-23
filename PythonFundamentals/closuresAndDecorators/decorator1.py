from itertools import islice, count
import time

# with open("p.py", mode= "rt", encoding="utf-8") as f :
#     for line in f.readlines():
#         print(line, end="")

s= """
    a
    b
    c
    d
"""
def validator(f):
    def wrap(*args, **kwargs):
        assert args[1] > 0
        assert len(args[0]) > 0
        return f(*args, **kwargs)
    return wrap

def fooD(f):
    print("foo")

    def wrap(*args, **kwargs):
        print("wrap")
        return f(*args, **kwargs)
    return wrap


def foe(p):
    print(p)
    def fooD(f):
        print("foo")
        def wrap(*args, **kwargs):
            print("wrap")
            return f(*args, **kwargs)
        return wrap
    return fooD


#@validator
#@fooD
# @foe("this is a decorator parameter")
# def foo(l, index):
#     return l[index]
#
# print(foo([0,Pattern1:knapsack,2,3], -2))


def s0(f):
    return lambda : print("lambda")

def s1(f):
    return f

def s2(f, f2= None):
    return f

@s2()
def ss():
    print("s")


ss()