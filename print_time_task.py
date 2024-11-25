"""Write a decorator @print_time.
This decorator should print how long the called function took to run."""

import time

def print_time(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        passed_time = end_time - start_time
        print(f"The total time of te function execution was {passed_time} seconds.")
        return result
    return deco

@print_time
def some_function():
    time.sleep(3)
    print("Done.")

some_function()

