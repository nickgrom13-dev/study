"""Напишите функцию get_middle(start, end),
которая находит среднее арифметическое значение в отрезке от start до end"""

def get_middle(start: int, end: int) -> float:
    """Функция, которая вычисляет среднее арифметическое в заданном отрезке"""
    return (start + end) / 2

a = input("Введите значение a\n")
b = input("Введите значение b\n")

if a.isdigit() and b.isdigit():
    print(f"Среднее арифметическое в отрезке [{a}, {b}] равно {get_middle(int(a), int(b))}")
else:
    print("Введены некорректные значения")