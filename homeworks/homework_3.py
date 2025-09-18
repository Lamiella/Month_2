from datetime import datetime, date

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def introduce(self):
        print(f'\nПривет, меня зовут {self.name}.'
              f'\nМне {self.age} лет.'
              f'\nМой день рождения - {self.birth_date}.'
              f'\nМоя работа - {self.occupation}.'
              f'\nВысшее образование: {"Есть" if self.higher_education else "Отсутствует"}.')

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        birth_date = datetime.strptime(self.birth_date, "%d.%m.%Y").date()
        today = date.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f'\nПривет, меня зовут {self.name}.'
              f'\nМне {self.age} лет.'
              f'\nМой день рождения - {self.birth_date}.'
              f'\nМоя работа - {self.occupation}.'
              f'\nВысшее образование: {"Есть" if self.higher_education else "Отсутствует"}.'
              f'\n{self.group_name} - место, где мы учимся вместе с Танджиро.')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'\nПривет, меня зовут {self.name}.'
              f'\nМне {self.age} лет.'
              f'\nМой день рождения - {self.birth_date}.'
              f'\nМоя работа - {self.occupation}.'
              f'\nВысшее образование: {"Есть" if self.higher_education else "Нет"}.'
              f'\nМоё хобби - {self.hobby}.')

tanjiro = Person(
    'Танджиро',
    '14.07.1900',
    'Охотник на демонов',
    False
)

classmate_1 = Classmate(
    'Зенитсу',
    '3.09.1900',
    'Охотник на демонов',
    False,
    'Корпус Убийц Демонов'
)

classmate_2 = Classmate(
    'Иноске',
    '22.04.1900',
    'Охотник на демонов',
    False,
    'Корпус Убийц Демонов'
)

friend_1 = Friend(
    'Нэдзуко',
    '28.12.1900',
    'Демон',
    False,
    'Путешествовать с братом'
)

friend_2 = Friend(
    'Гию Томиока',
    '8.02.1899',
    'Столп воды',
    True,
    'Созерцать воду'
)

for prsn in [tanjiro, classmate_1, classmate_2, friend_1, friend_2]:
    prsn.introduce()