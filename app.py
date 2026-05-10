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

class Exercise2:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return  (2*(self.length + self.breadth )) 

rectangle = Exercise2(20, 10)
print(f'Perimeter is {rectangle.perimeter()}')


class Exercise3:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f'Balance is {self.balance}')

sravani_account = Exercise3('Sravani', 1000)
sravani_account.display_balance()
