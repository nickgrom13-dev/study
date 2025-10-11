"""
Модуль CurrencyConverter определяет класс CurrencyConverter для управления конвертации валюты.
"""
from ExchangeRate import ExchangeRate

class CurrencyConverter:
    def __init__(self, rates:list[ExchangeRate]):
        self.rates = rates

    def get_exchange_rate(self, id_rate:int)->ExchangeRate|None:
        for rate in self.rates:
            if id_rate == rate.id_rate:
                return rate
        return None

    @staticmethod
    def convert(amount:int, from_currency:ExchangeRate, to_currency:ExchangeRate)->float|None:
        try:
            amount_in_rubles = amount / from_currency.rate
            converted_amount = amount_in_rubles * to_currency.rate
            return round(converted_amount, 3)
        except ValueError as error:
            print(f"Ошибка: {error}")

    @staticmethod
    def is_float(value: str) -> bool:
        """
        Проверяем, является ли введенное значение дробным числом
        :param value: Значение, которое нужно проверить.
        :return: Возвращает True, если дробное число, иначе возвращает False.
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    def show_rates(self):
        for rate in self.rates:
            print(rate)
        print("=" * 50)
