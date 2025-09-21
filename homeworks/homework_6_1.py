from datetime import datetime as dt
from time import sleep

def checktime(func):
    def wrapper(*args, **kwargs):
        start_time = dt.now()
        print(f'Функция была вызвана в {start_time.hour}:{start_time.minute}:{start_time.second} '
              f'{start_time.day}/{start_time.month}/{start_time.year}')
        result = func(*args, **kwargs)
        end_time = dt.now()
        print(f'Функция была закончена в {end_time.hour}:{end_time.minute}:{end_time.second} '
              f'{end_time.day}/{end_time.month}/{end_time.year}')
        return result
    return wrapper

@checktime
def hello_world():
    print("hello world")
    sleep(1)

hello_world()