import time

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called")
        start_time = time.time()       

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.2f} seconds.")
        return result
    return wrapper

@log_function_call
def say_hello(name):
    time.sleep(2)
    print(f"Hello, {name}!")

say_hello("Adeel")