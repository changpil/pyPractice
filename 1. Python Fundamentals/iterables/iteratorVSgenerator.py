class fib_iterator:
    def __init__(self):
        self.prev = 0
        self.curr = 1
    def __iter__(self):
        return self

    def __next__(self):
        v = self.curr
        self.curr = self.prev + self.curr
        self.prev = v
        return v


from my_practice import itertools

f1 = fib_iterator()
for i in itertools.islice(f1, 0, 10): print(i)

def fib_generator():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

f2= fib_generator()
for i in itertools.islice(f2, 10): print(i)



for i in itertools.islice(f1, 0, 10): print(i)



for i in itertools.islice(f2, 10): print(i)