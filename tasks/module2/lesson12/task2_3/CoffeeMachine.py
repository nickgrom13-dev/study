"""
Класс CoffeeMachine определяет процесс приготовления кофе.
"""
from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    __MAX_WATER_VOLUME = 1000 #Максимальный объем резервуара с водой.
    __MAX_COUNT_BEANS = 300 #Максимальный объем контейнера с зернами.
    __MAX_MILK_VOLUME = 400 #Максимальный объем резервуара с молоком.
    is_on = False #Статус кофемашины (включена, выключена).
    water_volume = __MAX_WATER_VOLUME #Объем воды (мл).
    count_beans = __MAX_COUNT_BEANS #Количество кофейных зерен (г).
    milk_volume = __MAX_MILK_VOLUME #Объем молока (мл).

    @abstractmethod
    def get_water(self):
        """
        Процесс получения воды для приготовления кофе.
        """
        pass

    @abstractmethod
    def get_beans(self):
        """
        Процесс получения зерен для приготовления кофе.
        """
        pass

    @abstractmethod
    def get_milk(self):
        """
        Процесс получения молока для приготовления кофе.
        """
        pass

    @staticmethod
    def get_max_water_volume()->int:
        """
        Геттер для получения объема резервуара для воды.
        :return: Максимальный объем резервуара для воды.
        """
        return CoffeeMachine.__MAX_WATER_VOLUME

    @staticmethod
    def get_max_beans_count()->int:
        """
        Геттер для получения объема контейнера для зерен.
        :return: Максимальный объем контейнера для зерен.
        """
        return CoffeeMachine.__MAX_COUNT_BEANS

    @staticmethod
    def get_max_milk_volume()->int:
        """
        Геттер для получения объема резервуара для молока.
        :return: Максимальный объем резервуара для молока.
        """
        return CoffeeMachine.__MAX_MILK_VOLUME

    def heat_water(self)->bool:
        """
        Процесс нагрева воды.
        """
        if CoffeeMachine.water_volume >= self.get_water():
            CoffeeMachine.water_volume -= self.get_water()
            print(f"> Нагреваем {self.get_water()} мл воды...\n")
            return True
        else:
            print(f"Ошибка: Недостаточно воды! Осталось {CoffeeMachine.water_volume} мл.\n")
            return False

    def grind_coffee(self)->bool:
        """
        Процесс помола зерен.
        """
        if CoffeeMachine.count_beans >= self.get_beans():
            CoffeeMachine.count_beans -= self.get_beans()
            print(f"> Перемалываем {self.get_beans()} г кофейных зерен...\n")
            return True
        else:
            print(f"Ошибка: Недостаточно кофейных зерен! Осталось {CoffeeMachine.count_beans} г.\n")
            return False

    def heat_milk(self)->bool:
        """
        Процесс нагрева молока.
        """
        if CoffeeMachine.milk_volume >= self.get_milk():
            CoffeeMachine.milk_volume -= self.get_milk()
            print(f"> Нагреваем {self.get_milk()} мл молока...\n")
            return True
        else:
            print(f"Ошибка: Недостаточно молока! Осталось {CoffeeMachine.milk_volume} мл.\n")
            return False

    @staticmethod
    def brew_coffee()->None:
        """
        Процесс заваривания кофе.
        """
        print("Завариваем кофе...\n")



