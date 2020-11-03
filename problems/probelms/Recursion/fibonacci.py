
import time, timeit
from datetime import timedelta



# O(n)
def fibonacci(n):
    init_1  = 1
    init_2 = 1

    if n < 3:
        return init_1

    for i in range (2, n):
        temp = init_2
        init_2 = init_1 + init_2
        init_1 = temp

    return init_2




# O(2^n)
def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


# O(n)
def fibonacci_rec2(n,lib=[0,1]):
    if n == 0 or n == 1:
        return lib[n]
    try:
        return lib[n]
    except:
        lib.append(fibonacci_rec2(n-1, lib) + fibonacci_rec2(n-2, lib))
        return lib[n]


n=50

start_time = time.clock()
a=fibonacci(n)
elapsed = time.clock() - start_time
print("Bottom-up {} : {} : {}".format(n,a,str(timedelta(seconds=elapsed))))


start_time = timeit.timeit()
#a=fibonacci_rec(n)
elapsed = timeit.timeit() - start_time
print("Top-down O(n^2) {} : {} : {}".format(n,a,str(timedelta(elapsed))))

start_time = time.time()
a=fibonacci_rec2(n)
elapsed = time.time() - start_time
print("Top-Down O(n) {} : {} : {}".format(n,a,str(timedelta(elapsed))))