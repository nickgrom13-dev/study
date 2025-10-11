"""
Создать конвертер денежной валюты.
Программа работает с 3 типами валют: рубли, доллары, евро.
Необходимо запросить у пользователя входные и выходные данные.
Использовать классы и объекты."""

from Currency import Currency
from ExchangeRate import ExchangeRate
from CurrencyConverter import CurrencyConverter

rates = [
    ExchangeRate(Currency('RUB', 'Российский рубль'), 1),
    ExchangeRate(Currency('USD', 'Доллар США'), 0.012),
    ExchangeRate(Currency('EUR', 'Евро'), 0.011)
]

currency_converter = CurrencyConverter(rates)

print("=== КОНВЕРТЕР ВАЛЮТ ===\nСписок доступных валют:")
currency_converter.show_rates()

while True:
    command = input("Выберите действие:\n"
                    "1) Показать список валют\n"
                    "2) Произвести конвертацию валюты\n"
                    "3) Обновить курс валюты\n"
                    "0) Выход\n").strip()

    match command:
        case "1":
            currency_converter.show_rates()
        case "2":
            while True:
                amount = input("Введите сумму для конвертации\n").strip()
                if not amount.isdigit() or int(amount) == 0:
                    print(f"Введено некорректное значение {amount}.\nПовторите попытку.")
                    continue
                amount = int(amount)

                id_from_currency = input("Введите код исходной валюты из списка валют\n").strip()
                if not id_from_currency.isdigit():
                    print(f"Введено некорректное значение {id_from_currency}.\nПовторите попытку.")
                    continue
                from_currency = currency_converter.get_exchange_rate(int(id_from_currency))
                if not from_currency:
                    print(f"Валюты с кодом {id_from_currency} нет в списке.\nПовторите попытку.")
                    continue

                id_to_currency = input("Введите код целевой валюты из списка валют\n").strip()
                if not id_to_currency.isdigit():
                    print(f"Введено некорректное значение {id_to_currency}.\nПовторите попытку.")
                    continue
                to_currency = currency_converter.get_exchange_rate(int(id_to_currency))
                if not from_currency:
                    print(f"Валюты с кодом {id_to_currency} нет в списке.\nПовторите попытку.")
                    continue

                if from_currency == to_currency:
                    print("Исходная и целевая валюта совпадают. Конвертация не требуется.")
                    break

                result = currency_converter.convert(amount, from_currency, to_currency)
                print(f"")
                print(f"\n=== РЕЗУЛЬТАТ ===\n{amount:.3f} {from_currency.currency.code} "
                      f"= {result:.3f} {to_currency.currency.code}")
                break
        case "3":
            id_currency = input("Введите код валюты для обновления курса обмена\n").strip()
            if id_currency.isdigit():
                rate = currency_converter.get_exchange_rate(int(id_currency))
                if rate:
                    new_rate = input(f"Введите новый курс для валюты {rate.currency.code}\n").strip()
                    if CurrencyConverter.is_float(new_rate) and new_rate.find("-") == -1:
                        rate.update_rate(float(new_rate))
                        print(f"Для валюты {rate.currency.code} установлен новый курс {new_rate}\n")
                    else:
                        print(f"Введено некорректное значение {new_rate}.\n")
                else:
                    print(f"Валюты с кодом {id_currency} нет в списке.\n")
            else:
                print(f"Введено некорректное значение {id_currency}.\n")
        case "0":
            break
        case _:
            print(f'Введен несуществующий пункт меню "{command}"\n')