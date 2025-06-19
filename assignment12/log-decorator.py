import logging
from functools import wraps

# --- One-time logger setup ---
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# --- Decorator Definition ---
def logger_decorator(func):
    def wrapper(*args, **kwargs):
    
        # Логируем сразу, без сборки message в одну строку
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {func(*args, **kwargs)}")

    return wrapper

# --- Function 1: no parameters, no return ---
@logger_decorator
def say_hello():
    print("Hello, World!")

# --- Function 2: variable number of positional arguments ---
@logger_decorator
def check_args(*args):
    return True

# --- Function 3: variable keyword arguments, returns the decorator itself ---
@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

# --- Mainline code ---
if __name__ == "__main__":
    say_hello()

    check_args(1, 2, 3, "hello", 5.5)

    return_decorator(a=1, b="test", debug=True)

    print("Function calls completed. Check decorator.log for details.")