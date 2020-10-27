def foo():
    h = "hello"
    for _ in range(3):
        j = "john"
        print(h)

    print(j)
foo()

print("-"*30)
default = "Abocado"

def changeDefault():
    global default
    default = "Apple"

print("-"*30)
print(default)
changeDefault()
print(default)


print("-"*30)
def tryfoo():
    try:
        _return = -1
        a = int("hello")
        _return = a
    except:
        pass
    return _return

print(tryfoo())

