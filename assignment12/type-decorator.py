def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)           # вызываем исходную функцию
            return type_of_output(x)            # преобразуем результат к нужному типу
        return wrapper
    return decorator

# Возвращает число 5, но декоратор преобразует его в строку
@type_converter(str)
def return_int():
    return 5

# Возвращает строку "not a number", а декоратор попытается сделать из неё int
@type_converter(int)
def return_string():
    return "not a number"

# Основная часть программы
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # Должно вывести "str"

    try:
        y = return_string()
        print("shouldn't get here!")  # Не должно выполниться
    except ValueError:
        print("can't convert that string to an integer!")