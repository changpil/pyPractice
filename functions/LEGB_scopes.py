# Local Scope
def square(base):
     result = base ** 2
     print(f'The square of {base} is: {result}')
square(10)

# The Enclosing Scope
def outer_func():
     # This block is the Local scope of outer_func()
     var = 100  # A nonlocal var
     # It's also the enclosing scope of inner_func()
     def inner_func():
         # This block is the Local scope of inner_func()
         print(f"Printing var from inner_func(): {var}")
         print(f"Printing another_var from inner_func(): {another_var}")
     inner_func()
     print(f"Printing var from outer_func(): {var}")
     another_var = 200  # Error: This is defined after calling inner_func()
outer_func()
