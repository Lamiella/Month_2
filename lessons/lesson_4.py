# diamond problem - проблема, суть которой в том, в каком порядке вызываются методы классов

class Animal:
    def speak(self):
        print('Animal speaking')

class Cat(Animal):
    def speak(self):
        print('Meow')
        super().speak()

class Dog(Animal):
    def speak(self):
        print('Gav')
        super().speak()

class CatDog(Cat, Dog): # множественное наследование
    def speak(self):
        print('Meow-gav')
        super().speak() # следующий в цепочке наследования

kotopes = CatDog()
kotopes.speak()
print(CatDog.__mro__) # method resolution order (показывает порядок наследования)