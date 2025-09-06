class Car:
    # Инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f'Car {self.model} is driving to {location}')

class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

    def drive_to_location(self, location):
        print(f'Bus {self.model} is driving at {location}')

Bus_40 = Bus('yellow', 'Mercedes Benz', 40)
Bus_40.drive_to_location('Bishkek')
print(Bus_40.color)
