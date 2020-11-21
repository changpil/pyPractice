import sys
import contextlib

class LoggingContextManager:
    def __enter__(self):
        print("Logging context manger.__enter__()")
        return "You are in a with block"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Logging context manager.__exit__: normal exit detected")
        else:
            print("Logging context manager.__exit__:exception detected: "
                  "type={}, value={}, traceback={}".format(exc_type, exc_val, exc_tb))

# with LoggingContextManager() as cm:
#     print("Logging")

# with LoggingContextManager() as cm:
#     raise ValueError("Error in with statement")
#     print("Logging")

# try:
#     with LoggingContextManager() as cm:
#         raise ValueError("Error in with statement")
#         print("Logging")
# except ValueError:
#     print("ValueError detected")

# @contextlib.contextmanager
# def my_context_manager():
#     print("myconext manager")
#     try:
#         yield [knapsack,2,3]
#         print("Context Manget after yield")
#
#     except Exception:
#         #print("logging conext manager",  sys.exc_info())
#         raise

# with my_context_manager() as cm:
#     print("context manager {!r}".format(cm))

# print()
#
# with my_context_manager() as cm:
#     raise ValueError("Something went wrong")
#     print("context manager {!r}".format(cm))