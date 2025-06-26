import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end - start:.4f} сек")
        return result
    return wrapper

@timer
def sleep_half():
    time.sleep(0.5)

sleep_half()