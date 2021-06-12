class MyNumbers:
  def __iter__(self, limit = 10):
    self.a = 1
    self.limit = limit
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    if x > self.limit:
        raise StopIteration
    return x

n = MyNumbers()

# i = 0
# while i < 200:
#     print(next(it))
#     i += 1

# for i in iter(n):
#     print(i)
#
# for i in n:
#     print(i)

it = iter(n)
v = next(it,None)
while v!= None:
    print(v)
    v = next(it, None)

