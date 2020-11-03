import itertools
for k , c in itertools.groupby("12345"):
    print(k, list(c))

print()
for k , c in itertools.groupby("11222334"):
    print(k, list(c))

print()
for k , c in itertools.groupby("555511222334"):
    print(k, list(c))

print()
st=""
for k , c in itertools.groupby("Aword winning 555511222334"):
    l =list(c)
    print(k, l)
    st +="".join(l)
print(st)