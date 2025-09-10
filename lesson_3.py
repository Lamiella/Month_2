# git log - посмотреть коммиты
# git checkout -b название - создать ветку и перейти в неё
# git switch имя - переключиться на другую ветку
# git branch - показывает все ветки проекта и ту в которой находишься

class Car:
    # Инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False # Защищённый атрибут (одно подчёркивание) - договорённость программистов "не трогать напрямую"
        self.__fined = False # Приватные атрибуты (два подчёркивания) - их нельзя вызвать напрямую снаружи (они "спрятаны")
        self.__max_speed = 100

    def drive_to_location(self, location):
        print(f'Car {self.model} is driving to {location}')

    # Приватный метод (доступен только внутри класса)
    def __test_car(self):
       print('test car')

    def get_fined(self):
        # Getter - метод для доступа к приватному атрибуту __fined
        return self.__fined

    def set_fined(self, fined):
        # Setter - метод для изменения приватного атрибута __fined
        self.__fined = fined

    # Декоратор @property позволяет обращаться к методу как к атрибуту
    @property
    def max_speed(self):
        return self.__max_speed

car_honda = Car('silver', 'honda')

# Доступ к защищённому атрибуту _fined (можно, но не рекомендуется)
print(car_honda._fined)

# Доступ к приватному атрибуту напрямую вызовет ошибку:
# print(car_honda.__fined) # AttributeError

# Правильный способ - через getter/setter
print(car_honda.get_fined())
car_honda.set_fined(True)
print(car_honda.get_fined())

# Доступ к приватному атрибуту __max_speed через property
print(car_honda.max_speed)