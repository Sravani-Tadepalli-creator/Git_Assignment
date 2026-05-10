import math


class Exercise1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

person1 = Exercise1('Sravani', 38)
person1.display_info()
