"""
Класс Espresso определяет процесс приготовления эспрессо.
"""
from CoffeeMachine import CoffeeMachine

class Espresso(CoffeeMachine):

    def get_water(self):
        return 40

    def get_beans(self):
        return 10

    def get_milk(self):
        return 0
