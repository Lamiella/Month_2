# Чтоб выйти из вима нужно нажать esc -> : и ввести wq, после этого слияние после конфликта завершится
# Dunder methods - magic methods double underscore (двойное подчёркивание)
# gt - greater than - self > other
# ge - greater than or equal: self => other
# it - less than: self <= other
# le - less than or equal: self <= other

from lessons.lesson_1 import Car

class Money:
    def __init__(self, amount=0):
        self.amount = amount

    def __str__(self): # встроенный метод для строк
        return f'Экземпляр Money: {self.amount}'

    def __add__(self, other): # встроенный метод для сложения
        return Money(self.amount + other.amount)

    def __sub__(self, other): # встроенный метод для вычитания
        return Money(self.amount - other.amount)

    def __mul__(self, other): # встроенный метод для умножения
        pass

    def __eq__(self, other): # встроенный метод для сравнения
        return self.amount == other.amount

    def __gt__(self, other): # встроенный метод для сравнения
        return self.amount > other.amount

igor_money = Money(100)
print(igor_money)

adilet_money = Money(250)
total_money = igor_money + adilet_money
print(total_money)

sub_money = adilet_money - igor_money
print(sub_money)

print(igor_money == adilet_money)
print(igor_money > adilet_money)

my_car = Car('red', 'honda')
print(my_car)