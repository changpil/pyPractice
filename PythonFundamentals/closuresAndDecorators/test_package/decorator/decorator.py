"""
def check_none_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError
            return f(*args)
        return wrap
    return validator

@check_none_negative(Pattern1:knapsack)
def create_list(value, size):
    return [value]*size


print(create_list(-10,-10))
"""
import unittest
def assertTrue(a):
    return a ==True

def assert_true(f):
    def wrap(*args,**kwargs):
        x = f(*args, **kwargs)
        print(*args)
        print(**kwargs)
        return assertTrue(x)
    return wrap

@assert_true
def test_decorator():
    return True


print(test_decorator())