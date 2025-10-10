"""Дополнительные функции"""

def get_id(str_atr:str, str_action:str)->int:
    """
    Ввод идентификатора с клавиатуры.
    :param str_atr: Наименование атрибута, для которого нужно ввести ID.
    :param str_action: Наименование действия, которое нужно совершить.
    :return: Введенный ID, или -1 в случае некорректного значения.
    """
    id_value = input(f'Введите ID {str_atr}, которого нужно {str_action}\n').strip()
    if id_value.isdigit():
        return int(id_value)
    else:
        print(f"Введено некорректное значение ID {str_atr}: {id_value}\n")
        return -1
