class Vehicle:
    def start(self):
        print('Vehicle starting')

class Car(Vehicle):
    def start(self):
        super().start()
        print('Car starting')

class ElectricCar(Vehicle):
    def start(self):
        super().start()

class Tesla(Car, ElectricCar):
    def start(self):
        super().start()
        print('Tesla ready')

Tesla().start()