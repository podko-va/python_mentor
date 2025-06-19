def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с аргументами: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

multiply(3, 7)