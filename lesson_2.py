# Родитель, суперкласс
class Car:
    # Инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f'Car {self.model} is driving to {location}')

# Дочерний класс, потомок, подкласс
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    # Переопределяем метод в дочернем классе. сигнатура должна совпадать
    def drive_to_location(self, location):
        print(f'Bus {self.model} is driving at {location}')

    # другой метод, которого нет в родительском классе
    def test_bus(self):
        print(f"Bus test {self.color}")

Bus_40 = Bus('yellow', 'Mercedes Benz', 40)
Bus_40.drive_to_location('Bishkek')
print(Bus_40.color)

car_honda = Car("black", "Honda Civic")
car_honda.drive_to_location("Karakol")