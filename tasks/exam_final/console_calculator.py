"""
    Консольный вариант: Программа должна запрашивать у пользователя ввод выражения в виде 2 + 3
    и выводить результат операции в виде 2 + 3 = 5. В случае ввода некорректного значения
    сообщаем об ошибке и просим заново ввести корректное выражение.
"""
import re

def is_correct_expression(expression:str) -> bool:
    """
    Проверяет, корректно ли введено выражение для вычисления
    :param expression: выражение, которое нужно проверить
    :return: True - выражение введено корректно, иначе False
    """
    rule = r'\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*'
    if re.match(rule, expression):
        return True
    else:
        return False

def main():

    print('=' * 50)
    print('КОНСОЛЬНЫЙ ПРОСТОЙ КАЛЬКУЛЯТОР')
    print('=' * 50)
    print("Примеры: 2 + 3, 10.1 * 5, -8 / 2")
    print("Поддерживаемые операторы: +, -, *, /")
    print('-' * 50)

    while True:

        expression = input('Введите выражение для вычисления:\n').strip()

        if not is_correct_expression(expression):
            print(f'Ошибка: введено некорректное выражение "{expression}", повторите попытку ввода')
            continue

        try:
            result = eval(expression)
            print(f'{expression} = {result}')
        except ZeroDivisionError as e:
            print(f'Ошибка: деление на ноль, повторите попытку ввода')
            continue
        except Exception as e:
            print(f'Ошибка: {e}, повторите попытку ввода')
            continue

        while True:
            answer = input('Вычислить еще одно выражение? (y/n):\n').strip().lower()
            if answer in ['да', 'д', 'yes', 'y', 'у']:
                break
            elif answer in ['нет', 'н', 'no', 'n']:
                print("Программа завершена.")
                return
            else:
                print("Пожалуйста, введите 'y' или 'n'")

if __name__ == "__main__":
    main()