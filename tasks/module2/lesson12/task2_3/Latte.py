"""
Класс Latte определяет процесс приготовления латте.
"""
from CoffeeMachine import CoffeeMachine

class Latte(CoffeeMachine):

    def get_water(self):
        return 60

    def get_beans(self):
        return 20

    def get_milk(self):
        return 150
