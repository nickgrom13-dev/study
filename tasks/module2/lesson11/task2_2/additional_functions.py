"""Дополнительные функции"""

def get_id(text:str)->int:
    """
    Ввод идентификатора с клавиатуры.
    :param text: Текст ввода.
    :return: Введенный ID, или -1 в случае некорректного значения.
    """
    id_value = input(text).strip()
    if id_value.isdigit():
        return int(id_value)
    else:
        print(f"Введено некорректное значение ID: {id_value}\n")
        return -1

def get_amount(text:str)->float|int:
    """
    Ввод суммы с клавиатуры.
    :param text: Текст ввода.
    :return: Введенную сумму, или -1 в случае некорректного значения.
    """
    amount = input(text).strip()
    if is_positive_float(amount):
        return float(amount)
    else:
        print(f"Введено некорректное значение {amount}.\n")
        return -1

def is_positive_float(value: str) -> bool:
    """
    Проверяем, является ли введенное значение положительным дробным числом
    :param value: Значение, которое нужно проверить.
    :return: Возвращает True, если положительное число, иначе возвращает False.
    """
    try:
        return value.find("-") == -1 and float(value) > 0
    except ValueError:
        return False