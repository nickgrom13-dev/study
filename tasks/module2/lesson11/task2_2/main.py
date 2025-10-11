"""
Создать конвертер денежной валюты.
Программа работает с 3 типами валют: рубли, доллары, евро.
Необходимо запросить у пользователя входные и выходные данные.
Использовать классы и объекты."""

from Currency import Currency
from ExchangeRate import ExchangeRate
from CurrencyConverter import CurrencyConverter
from additional_functions import get_amount, get_id

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
                amount = get_amount("Введите сумму для конвертации\n")
                if amount == -1:
                    print("Повторите попытку")
                    continue

                id_from_currency = get_id("Введите код исходной валюты из списка валют\n")
                if id_from_currency == -1:
                    print("Повторите попытку")
                    continue
                from_currency = currency_converter.get_exchange_rate(id_from_currency)
                if not from_currency:
                    print("Повторите попытку")
                    continue

                id_to_currency = get_id("Введите код целевой валюты из списка валют\n")
                if id_to_currency == -1:
                    print("Повторите попытку")
                    continue
                to_currency = currency_converter.get_exchange_rate(id_to_currency)
                if not to_currency:
                    print("Повторите попытку")
                    continue

                if from_currency == to_currency:
                    print("Исходная и целевая валюта совпадают. Конвертация не требуется.")
                    break

                result = currency_converter.convert(amount, from_currency, to_currency)
                print(f"\n=== РЕЗУЛЬТАТ ===\n{amount:.3f} {from_currency.currency.code} "
                      f"= {result:.3f} {to_currency.currency.code}")
                break
        case "3":
            id_currency = get_id("Введите код валюты для обновления курса обмена\n")
            if id_currency != -1:
                rate = currency_converter.get_exchange_rate(int(id_currency))
                if rate:
                    new_rate = get_amount(f"Введите новый курс для валюты {rate.currency.code}\n")
                    if new_rate != -1:
                        rate.update_rate(float(new_rate))
                        print(f"Для валюты {rate.currency.code} установлен новый курс {new_rate}\n")
        case "0":
            break
        case _:
            print(f'Введен несуществующий пункт меню "{command}"\n')