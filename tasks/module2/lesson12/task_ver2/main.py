"""
Понять принцип абстракции на примере создания класса кофемашины.
Скрыть сложные внутренние процессы за простым интерфейсом
"""
from CoffeeMachineOperation import CoffeeMachineOperation
from Espresso import Espresso
from Latte import Latte
from Capuccino import Capuccino

coffee_machine = CoffeeMachineOperation

while True:

    if coffee_machine.check_status():
        while True:
            command = input("Меню:\n"
                            "1) Показать текущие ресурсы\n"
                            "2) Приготовить эспрессо\n"
                            "3) Приготовить латте\n"
                            "4) Приготовить капучино\n"
                            "5) Добавить воды\n"
                            "6) Добавить зерна\n"
                            "7) Добавить молоко\n"
                            "0) Выключить кофемашину\n").strip()

            match command:
                case "1":
                    coffee_machine.show_remaining_resources()
                case "2":
                    espresso = Espresso()
                    if espresso.heat_water():
                        if espresso.grind_coffee():
                            espresso.brew_coffee()
                            print("Ваш эспрессо готов\n")
                case "3":
                    latte = Latte()
                    if latte.heat_water():
                        if latte.grind_coffee():
                            if latte.heat_milk():
                                latte.brew_coffee()
                                print("Ваш латте готов\n")
                case "4":
                    capuccino = Capuccino()
                    if capuccino.heat_water():
                        if capuccino.grind_coffee():
                            if capuccino.heat_milk():
                                capuccino.brew_coffee()
                                print("Ваш капучино готов\n")
                case "5":
                    new_volume = input("Введите количество воды для добавления в кофемашину\n").strip()
                    if new_volume.isdigit():
                        coffee_machine.add_water(int(new_volume))
                    else:
                        print(f"Введено некорректное значение: {new_volume}\n")
                case "6":
                    new_count = input("Введите количество зерен для добавления в кофемашину\n").strip()
                    if new_count.isdigit():
                        coffee_machine.add_beans(int(new_count))
                    else:
                        print(f"Введено некорректное значение: {new_count}\n")
                case "7":
                    new_volume = input("Введите количество молока для добавления в кофемашину\n").strip()
                    if new_volume.isdigit():
                        coffee_machine.add_milk(int(new_volume))
                    else:
                        print(f"Введено некорректное значение: {new_volume}\n")
                case "0":
                    coffee_machine.turn_off()
                    break
                case _:
                    print(f"Введена неверная команда: {command}\n")
    else:
        answer = input("Включить кофемашину? (y, n)\n").strip().lower()
        if answer == 'y':
            coffee_machine.turn_on()
        elif answer == 'q':
            break
