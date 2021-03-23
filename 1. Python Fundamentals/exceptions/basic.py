# IndexError: l[4]
# KeyError: d["h"]
# ValueErroe: int("hello")
# TypeError: Pattern1:knapsack.2 + "ss"
# if not isInstance(*s, str):
#       raise TypeError()


def convert( s):
    try:
        x = int(s)
        print("coverted")
    except ValueError:
        print("ValueError")
    except TypeError:
        print("Type Error")

try:
   s =  input("enter: ")
   convert(s)
except Exception as e:
    print(e)
except (ValueError, TypeError) as e:
    print(e)