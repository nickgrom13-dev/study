"""
Модуль ExchangeRate определяет класс ExchangeRate для управления информацией об обменных курсах.

Класс ExchangeRate предоставляет функциональность для:
- Обновления обменного курса.
"""
from Currency import Currency

class ExchangeRate:
    id_rate = 0
    def __init__(self, currency:Currency, rate:float):
        ExchangeRate.id_rate +=1
        self.id_rate = ExchangeRate.id_rate
        self.currency = currency
        self.rate = rate
    def __str__(self):
        return f"{self.id_rate}) {self.currency} имеет курс: {self.rate}"

    def update_rate(self, new_rate:float)->None:
        """
        Обновление обменного курса.
        :param new_rate: Значение нового обменного курса
        """
        self.rate = new_rate