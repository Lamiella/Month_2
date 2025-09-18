class Distance:

    unit_type = {'cm': 0.01, 'm': 1, 'km': 1000}

    def __init__(self, value, unit='m'):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f'Значение: {self.value}, единица измерения: {self.unit}'

    def __add__(self, other):
        return Distance(self.convert() + other.convert())

    def __sub__(self, other):
        total = self.convert() - other.convert()

        if total < 0:
            return 'Значение не может быть отрицательным'

        return Distance(total, 'm')

    def __eq__(self, other):
        return self.convert() == other.convert()

    def convert(self):
        return self.value * self.unit_type[self.unit]