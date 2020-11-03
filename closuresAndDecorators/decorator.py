class Trace1:
    def __init__(self):
        self.name="Trace1"

    def __call__(self, f):
        def wrap(*args, **kwargs):
            print("Calling Trace1 {}".format(f))
            return f(*args, **kwargs)
        return wrap

class Trace2:
    def __init__(self, f):
        self.f = f
        self.name= "Trace2"

    def __call__(self, *args, **kwargs):
        print("Calling Trace 2 {}".format(self.f))
        return self.f(*args, **kwargs)


@Trace1()
def fun():
    print("fun")

@Trace2
def fun2():
    print("fun2")

fun()
fun2()

#print(fun.name) #Error
print(fun2.name)
