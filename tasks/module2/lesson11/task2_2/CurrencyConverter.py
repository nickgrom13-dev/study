"""
Модуль CurrencyConverter определяет класс CurrencyConverter для управления конвертации валюты.

Класс CurrencyConverter предоставляет функциональность для:
- Вывод информации об доступных обменных курсах.
- Для поиска данных об обменном курсе валюты с определенным идентификатором.
- Конвертации определенной суммы с одной валюты на другую.
"""
from ExchangeRate import ExchangeRate

class CurrencyConverter:
    def __init__(self, rates:list[ExchangeRate]):
        self.rates = rates

    def show_rates(self)->None:
        """
        Вывод информации об доступных обменных курсах.
        """
        for rate in self.rates:
            print(rate)
        print("=" * 50)

    def get_exchange_rate(self, id_rate:int)->ExchangeRate|None:
        """
        Поиск обменного курса по идентификатору.
        :param id_rate: Идентификатор обменного курса, который нужно найти.
        :return: Найденный обменный курс, объект класса ExchangeRate,
                    или None в случае, если обменный курс не найден.
        """
        for rate in self.rates:
            if id_rate == rate.id_rate:
                return rate
        print(f"Валюты с кодом {id_rate} нет в списке.\n")
        return None

    @staticmethod
    def convert(amount:float, from_currency:ExchangeRate, to_currency:ExchangeRate)->float|None:
        """
        Конвертация определенной суммы с одной валюты на другую.
        :param amount: Сумма, которую нужно конвертировать из одной валюты в другую.
        :param from_currency: Валюта, которую нужно конвертировать.
        :param to_currency: Валюта, из которой нужно конвертировать.
        :return: Результат конвертации.
        """
        try:
            amount_in_rubles = amount / from_currency.rate
            converted_amount = amount_in_rubles * to_currency.rate
            return round(converted_amount, 3)
        except ValueError as error:
            print(f"Ошибка: {error}")