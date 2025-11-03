"""Создать программу на Python для решения квадратного уравнения."""
import math

def is_float(value:str)->bool:
    """ Проверяем, является ли введенное значение дробным числом"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_value(name_var:str)->float:
    """Вводим значение коэффициента. Ввод повторяется до тех пор,
       пока не будет указано корректное значение"""
    while 1:
        value = input(f"Введите коэффициент {name_var}\n").strip()
        if is_float(value):
            return float(value)
        print(f"Введено некорректное значение для коэффициента {name_var}. "
              f"Повторите попытку ввода.")

a = get_value("a")
b = get_value("b")
c = get_value("c")

if a != 0:
    print(f"Найдем решение квадратного уравнения для коэффициентов: a = {a}, b = {b}, c = {c}")
    d = round(b ** 2 - 4 * a * c, 5)
    print(f"Дискриминант D равен {d}")
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Уравнение имеет два корня: {format(x1, ".5f")} и {format(x2, ".5f")}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Уравнение имеет один корень: {format(x, ".5f")}")
    else:
        print("Уравнение не имеет корней")
else:
    print("Это не квадратное уравнение, так как коэффициент a равен 0")
