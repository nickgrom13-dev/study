"""
Класс CoffeeMachineOperation определяет процесс управления кофемашиной.
"""
from CoffeeMachine import CoffeeMachine
from Capuccino import Capuccino
from Latte import Latte

class CoffeeMachineOperation:

    def __init__(self, coffee_types:list[dict[str, CoffeeMachine]]):
        self.coffee_types = coffee_types

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
    def check_status()->bool:
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
        max_volume = CoffeeMachine.get_max_water_volume()
        if new_volume > max_volume:
            print(f"Ошибка: вода в количестве {additional_volume} мл "
                  f"не поместится в резервуар кофемашины объемом {max_volume} мл!\n"
                  f"Текущий объем воды в резервуаре: {CoffeeMachine.water_volume} мл.\n")
        else:
            CoffeeMachine.water_volume = new_volume
            print(f"В резервуар добавлена вода в количестве {additional_volume} мл.\n"
                  f"Текущий объем воды в резервуаре: {CoffeeMachine.water_volume} мл.\n")

    @staticmethod
    def add_beans(additional_count)->None:
        """
        Добавление зерен в кофемашину
        :param additional_count: количество зерен, которое добавляется в кофемашину
        """
        new_count = CoffeeMachine.count_beans + additional_count
        max_count = CoffeeMachine.get_max_beans_count()
        if new_count > max_count:
            print(f"Ошибка: зерна в количестве {additional_count} г "
                  f"не поместятся в контейнер кофемашины объемом {max_count} г!\n"
                  f"Текущий объем зерен в контейнере: {CoffeeMachine.count_beans} г.\n")
        else:
            CoffeeMachine.count_beans = new_count
            print(f"В контейнер добавлены зерна в количестве {additional_count} г.\n"
                  f"Текущий объем зерен в контейнере: {CoffeeMachine.count_beans} г.\n")

    @staticmethod
    def add_milk(additional_volume)->None:
        """
        Добавление молока в кофемашину
        :param additional_volume: количество молока, которое добавляется в кофемашину
        """
        new_volume = CoffeeMachine.milk_volume + additional_volume
        max_volume = CoffeeMachine.get_max_milk_volume()
        if new_volume > max_volume:
            print(f"Ошибка: молоко в количестве {additional_volume} мл "
                  f"не поместится в резервуар кофемашины объемом {max_volume} мл!\n"
                  f"Текущий объем молока в резервуаре: {CoffeeMachine.milk_volume} мл.\n")
        else:
            CoffeeMachine.milk_volume = new_volume
            print(f"В резервуар добавлено молоко в количестве {additional_volume} мл.\n"
                  f"Текущий объем молока в резервуаре: {CoffeeMachine.milk_volume} мл.\n")

    @staticmethod
    def show_remaining_resources()->None:
        """
        Вывод сообщения об оставшихся ресурсах кофемашины.
        """
        print(f"В кофемашине осталось:\nводы - {CoffeeMachine.water_volume} мл,"
              f"\nкофейных зерен - {CoffeeMachine.count_beans} г, "
              f"\nмолока - {CoffeeMachine.milk_volume} мл.\n")

    def make_coffee(self, name_type:str)->None:
        """
        Процесс приготовления выбранного напитка
        :param name_type: Наименование напитка, который нужно приготовить
        """
        coffee_type = None
        for item in self.coffee_types:
            if item["coffee_type"] == name_type:
                coffee_type = item["class"]
        if coffee_type:
            if coffee_type.heat_water():
                if coffee_type.grind_coffee():
                    if isinstance(coffee_type, (Latte, Capuccino)):
                        if not coffee_type.heat_milk():
                            return
                    coffee_type.brew_coffee()
                    print(f"Ваш {name_type} готов\n")

    @staticmethod
    def get_volume(text: str)->int:
        """
        Ввод объема с клавиатуры.
        :param text: Текст ввода.
        :return: Введенное количество, или -1 в случае некорректного значения.
        """
        volume = input(text).strip()
        if volume.isdigit():
            return int(volume)
        else:
            print(f"Введено некорректное значение: {volume}\n")
            return -1
