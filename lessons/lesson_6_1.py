def printer(func): # кастомный декоратор
    def wrapper(*args, **kwargs):
        print(f'До вызова ф-ии {func.__name__}')
        result = func(*args, **kwargs)
        print(f'После вызова ф-ии {func.__name__}')
        return result
    return wrapper

@printer
def hello_world():
    print('hello world')

@printer
def add_numbers(num1, num2):
    return num1 + num2

hello_world()
print(add_numbers(1, 2))