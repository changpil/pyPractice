import generator

def lucas():
    yield 2
    a, b = 2, 1
    while True:
        yield  b
        a, b = b , a+b


for i in generator.take(10, lucas()):
    print(i)