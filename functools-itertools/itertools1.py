# ct = 0
# for i in itertools.count():
#     print(i, " ")
#     if ct == 100:
#         break
#     ct += 1
#
#
# ct = 0
# for i in itertools.cycle("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#     print(i, " ")
#     if ct == 100:
#         break
#     ct += 1
#
#
# for i in itertools.repeat(100, 100):
#     print(i, " ")


a =[1,2,3]
b=[3,4,5]
c=[5,6,7]

d = itertools.starmap(lambda x, y: x + y, zip(a, b))
d = itertools.starmap(lambda x, y, z: x + y + z, zip(a, b, c))
print(list(d))

for i in itertools.islice('ABCDEFG', 1, 4, 2):
    print(i)

for i in itertools.accumulate([1, 2, 3, 4, 5]):
    print(i)

for i in itertools.zip_longest('ABCD', 'xy', fillvalue='-'):
    print(i)

print()
for i in itertools.product("ABCD", repeat=2):
    print(i)

print()
for i in itertools.permutations("ABCD", 2):
    print(i)

print()
for i in itertools.combinations("ABCD", 2):
    print(i)


class Sensor:
    def __iter__(self):
        return self
    def __next__(self):
        import random
        return random.random()

sensor = Sensor()
import datetime
timestamps = iter(datetime.datetime.now, None)


for s, v in itertools.islice(zip(timestamps, sensor), 10):
    print(s,v)
    import time
    time.sleep(1)