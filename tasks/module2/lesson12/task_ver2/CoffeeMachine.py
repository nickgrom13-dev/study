"""
Класс CoffeeMachine определяет работу кофемашины.
"""

from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    is_on = False #Кофемашина включена
    water_volume = 1000 #Объем воды (мл)
    count_beans = 300 #Количество кофейных зерен (г)
    milk_volume = 400 #Объем молока (мл)

    @abstractmethod
    def get_water(self):
        pass

    @abstractmethod
    def get_beans(self):
        pass

    @abstractmethod
    def get_milk(self):
        pass

    @staticmethod
    def turn_on()->None:
        """
        Процесс включения кофемашины.
        """
        print("Включаем кофемашину...\n")
        CoffeeMachine.is_on = True
        print("Кофемашина готова к работе!\n")

    @staticmethod
    def turn_off()->None:
        """
        Процесс выключения кофемашины.
        """
        print("Выключаем кофемашину...\n")
        CoffeeMachine.is_on = False
        print("Кофемашина выключена.\n")

    @staticmethod
    def check_status() -> bool:
        """
        Проверка текущего статуса кофемашины.
        :return: True - если кофемашина включена, иначе False.
        """
        if not CoffeeMachine.is_on:
            print("Кофе машина выключена.")
        return CoffeeMachine.is_on

    @staticmethod
    def add_water(additional_volume)->None:
        """
        Добавление воды в кофемашину
        :param additional_volume: количество воды, которое добавляется в кофемашину
        """
        new_volume = CoffeeMachine.water_volume + additional_volume
        if new_volume > 1000:
            print(f"Ошибка: вода в количестве {additional_volume} мл "
                  f"не поместится в резервуар кофемашины объемом 1000 мл!\n")
        else:
            CoffeeMachine.water_volume = new_volume
            print(f"В резервуар добавлена вода в количестве {additional_volume} мл.\n"
                  f"Текущий объем в резервуаре: {CoffeeMachine.water_volume} мл.\n")

    @staticmethod
    def add_beans(additional_count)->None:
        """
        Добавление зерен в кофемашину
        :param additional_count: количество зерен, которое добавляется в кофемашину
        """
        new_count = CoffeeMachine.count_beans + additional_count
        if new_count > 300:
            print(f"Ошибка: зерна в количестве {additional_count} г "
                  f"не поместятся в контейнер кофемашины объемом 300 г!")
        else:
            CoffeeMachine.count_beans = new_count
            print(f"В контейнер добавлены зерна в количестве {additional_count} г.\n"
                  f"Текущий объем в контейнере: {CoffeeMachine.count_beans} г.\n")

    @staticmethod
    def add_milk(additional_volume)->None:
        """
        Добавление молока в кофемашину
        :param additional_volume: количество молока, которое добавляется в кофемашину
        """
        new_volume = CoffeeMachine.milk_volume + additional_volume
        if new_volume > 400:
            print(f"Ошибка: молоко в количестве {additional_volume} мл "
                  f"не поместится в резервуар кофемашины объемом 400 мл!\n")
        else:
            CoffeeMachine.milk_volume = new_volume
            print(f"В резервуар добавлено молоко в количестве {additional_volume} мл.\n"
                  f"Текущий объем в резервуаре: {CoffeeMachine.milk_volume} мл.\n")

    @staticmethod
    def show_remaining_resources() -> None:
        """
        Вывод сообщения об оставшихся ресурсах кофемашины.
        """
        print(f"В кофе-машине осталось:\nводы - {CoffeeMachine.water_volume} мл,"
              f"\nкофейных зерен - {CoffeeMachine.count_beans} г, "
              f"\nмолока - {CoffeeMachine.milk_volume} мл.\n")

    @staticmethod
    def brew_coffee()->None:
        """
        Процесс заваривания кофе.
        """
        print("Завариваем кофе...\n")

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





