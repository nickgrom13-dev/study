"""
Понять принцип абстракции на примере создания класса кофемашины.
Скрыть сложные внутренние процессы за простым интерфейсом
"""
from CoffeeMachineOperation import CoffeeMachineOperation
from Espresso import Espresso
from Latte import Latte
from Capuccino import Capuccino

coffee_types = [
{"coffee_type":"эспрессо", "class":Espresso()},
{"coffee_type":"латте", "class":Latte()},
{"coffee_type":"капучино", "class":Capuccino()}
]

coffee_machine = CoffeeMachineOperation(coffee_types)

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
                    coffee_machine.make_coffee("эспрессо")
                case "3":
                    coffee_machine.make_coffee("латте")
                case "4":
                    coffee_machine.make_coffee("капучино")
                case "5":
                    new_volume = coffee_machine.get_volume("Введите количество воды для добавления в кофемашину\n")
                    if new_volume != -1:
                        coffee_machine.add_water(new_volume)
                case "6":
                    new_count = coffee_machine.get_volume("Введите количество зерен для добавления в кофемашину\n")
                    if new_count != -1:
                        coffee_machine.add_beans(new_count)
                case "7":
                    new_volume = coffee_machine.get_volume("Введите количество молока для добавления в кофемашину\n")
                    if new_volume != -1:
                        coffee_machine.add_milk(new_volume)
                case "0":
                    coffee_machine.turn_off()
                    break
                case _:
                    print(f"Введена неверная команда: {command}\n")
    else:
        answer = input("Включить кофемашину? (1 - включить, 0 - выйти из программы)\n").strip()
        if answer == '1':
            coffee_machine.turn_on()
        elif answer == '0':
            break
        else:
            print(f"Введен некорректный ответ на вопрос: {answer}\n")

