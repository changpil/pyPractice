
def foo():
    for d in range(-1, 7):
        a = [1,2,3]
        print(d , end = "")
        if not 0 <= d < 5:
            print(" not")
        else:
            print(" in ")
    print(a)
print(foo())
