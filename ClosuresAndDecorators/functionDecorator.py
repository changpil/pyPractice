def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap   # should be callable

@escape_unicode
def korean_capital():
    return "seoul 서울특별시"

def korean_capital2():
    return "seoul 서울특별시"

a = korean_capital()
print(f"{type(a)}: {a}")
print(korean_capital2())



def escape_unicode2(f):
    x = f
    print("escape_unicode2")
    return x    # should be callable

@escape_unicode2
def korean_capital3():
    return "seoul 서울특별시"
print(korean_capital3())