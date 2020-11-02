
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


for i in take(3, [0,1,2,3,4,5]):
    print(i)

print("-"*30)

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

items = [2,3,1, 2, 4,7,3,1,4,6,9]

for item in take(4, distinct(items)):
    print(item)

print("-"*30)