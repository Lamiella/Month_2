class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print('\nИнформация о пользователе'
              f'\nИмя: {self.name}'
              f'\nДень рождения: {self.birth_date}'
              f'\nПрофессия: {self.occupation}'
              f'\nВысшее образование: {"Есть" if self.higher_education else "Нет"}')

person1 = Person('Наруто Узумаки', '10.10.1997', 'Ниндзя', True)
person2 = Person('Микаса Аккерман', '10.02.1999', 'Воин-разведчик', False)
person3 = Person('Лайт Ягами', '28.02.1999', 'Студент', True)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

person1.introduce()
person2.introduce()
person3.introduce()