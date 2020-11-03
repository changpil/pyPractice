


"""
implement linux tail commands
"""




def tail ( file , line):
    tail = [ ]
    with open(file, 'rt') as f:
        tail =  f.readlines()

    print(type(tail))
    print("#"*100)
    starting_line = len(tail) - line if len(tail) > line else 0

    return "".join(tail[starting_line:])

print(tail("string.txt", 5))
