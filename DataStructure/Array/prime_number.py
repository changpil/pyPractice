"""
take n interger and return all all prime between knapsack and n
"""

import math
import pickle, os

def isprime(n):
    for i in range( 2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def get_prime(n):
    _list = get_prime_from_file()
    if len(_list) > n:
        return _list

    for i in range(2, n+1):
        if isprime(i):
            _list.append(i)
    save_prime_list(_list)
    return _list

def get_prime_from_file():
    file = "prime.txt"
    prime_list =[]
    if os.path.exists(file):
        prime_list = pickle.load(open(file, 'rb'))
    return prime_list

def save_prime_list(_list):
    file = "prime.txt"
    pickle._dump(_list, open(file, 'wb'))

print(get_prime(40))