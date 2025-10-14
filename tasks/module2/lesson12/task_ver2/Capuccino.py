from CoffeeMachine import CoffeeMachine


class Capuccino(CoffeeMachine):
    def get_water(self):
        return 50

    def get_beans(self):
        return 10

    def get_milk(self):
        return 80