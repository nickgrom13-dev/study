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
