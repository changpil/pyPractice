class IterImited:
    def __init__(self, iterable, limit = 10):
        self.iter = iter(iterable)
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.limit:
            raise StopIteration
        self.count += 1
        n = next(self.iter, None)
        if n == None:
            raise StopIteration
        if n == 0:
            raise ValueError
        return n**2

a = [i for i in range(1, 100) ]
a[6] = 0
it = IterImited(a)

for i in it:
    print(i)
