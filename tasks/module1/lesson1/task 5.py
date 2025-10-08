"""Ввести год рождения в консоль. Вывести возраст. Текущий год используем 2025 в
явном виде, специальные функции для работы с датой использовать необязательно."""
from datetime import datetime

birth_year = int(input("Введите год рождения...\n"))
current_year = datetime.now().year
print(f"Возраст: {str(current_year - birth_year)}")