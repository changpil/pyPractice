def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

a = [1,2,3,4]

print(first(a))

print("-"*30)
def exceptfirst(iterable):
    iterator = iter(iterable)
    try:
        next(iterator)
        return iterator
    except StopIteration:
        raise ValueError("iterable is empty")

for i in exceptfirst(a):
    print(i)