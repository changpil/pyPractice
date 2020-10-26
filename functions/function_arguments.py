import math
def a(* args):
    print(f"lens {len(args)}")
    for i in args:
        print(f"{type(i)}: {i}")

a([1.3,4, "abc", math])
a(1.3,4,"abc", math)