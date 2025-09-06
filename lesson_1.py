# ООП - объектно-ориентированное программирование
# GIT - система контроля версий (git init)
# git config --global user.name 'Alena Kucherenko'
# git config --global user.email alenka110198@gmail.com
# Функции внутри класса - методы
# __init__ - конструктор для установления свойств объекта

class Car: # названия классов по принципу PascalCase - каждое слово с большой буквы
    # Инициализатор
    def __init__(self, color, model): # свойства (поля, атрибуты)
        self.color = color
        self.model = model

    def drive_to_location(self, location): # названия методов по принципу snake_case - каждое слово через '_'
        print(f'Car {self.model} is driving to {location}')

car_honda = Car('silver', 'honda') # объект класса (экземпляр, instance)
print(car_honda)

car_subaru = Car('black', 'subaru')
print(car_subaru)

car_subaru.drive_to_location('Bishkek')
car_honda.color = 'red'

print(f'Car color: {car_honda.color}, model: {car_honda.model}')
print(f'Car color: {car_subaru.color}, model: {car_subaru.model}')

print(type(car_honda))