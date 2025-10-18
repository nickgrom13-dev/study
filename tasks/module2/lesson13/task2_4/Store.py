"""
Абстрактный класс Store, в котором абстрактные методы: вывод списка товаров
"""
from abc import ABC, abstractmethod

class Store(ABC):
    @abstractmethod
    def show_items(self):
        pass
