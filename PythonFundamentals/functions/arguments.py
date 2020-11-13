def print_args1(*args, **kwargs):
    print(args)
    print(kwargs)

def print_border(s):
    print("-"*len(s))
    print(s)
    print("-" * len(s))
print_border('print_args()')
print_args1() # No error

def print_args2(arg, *args, kwarg, **kwargs):
    print(arg)
    print(args)
    print(kwarg)
    print(kwargs)

try:
    print_border('print_args2(10, k=20)')
    print_args2(10, k=20)
except Exception as e:
    print(e)

print_border('print_args2(10, kwarg=20)')
print_args2(10, kwarg=20)

print_border('print_args2(10,  kwarg=10, k=20, l=30)')
print_args2(10,  kwarg=10, k=20, l=30)


def print_args3(a1, a2, *a3):
    print(a1)
    print(a2)
    print(a3)

print_border("t = (11,22,33,44)\nprint_args3(t)")
t = (11,22,33,44)
try:
    print_args3(t)
except Exception as e:
    print(e)

print_border("t = (11,22,33,44)\nprint_args3(*t)")
t = (11,22,33,44)
print_args3(*t)


def print_args4(**kwargs):
    print(kwargs)
    for i, v in kwargs.items():
        print(f"{i} : {v}" )


print_border('k= {"1":2, "3":4, "5":6}\nprint_args4(k)')
k= {"1":2, "3":4, "5":6}
try:
    print_args4(k)
except Exception as e:
    print(e)

print_border('k= {"a":2, "b":4, "c":6}\nprint_args4(k)')
k= {"a":2, "b":4, "c":6}
try:
    print_args4(k)
except Exception as e:
    print(e)

print_border('k= {"a":2, "b":4, "c":6}\nprint_args4(k)')
k= {"a":2, "b":4, "c":6}
try:
    print_args4(**k)
except Exception as e:
    print(e)


print_border('k= {"1":2, "3":4, "5":6}\nprint_args4(k)')
k= {"1":2, "3":4, "5":6}
print_args4(**k)

