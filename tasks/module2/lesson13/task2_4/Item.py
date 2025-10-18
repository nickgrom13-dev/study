"""
Класс Item определяет свойства товара
"""
from Category import Category

class Item:
    count = 0 #Счетчик для id

    def __init__(self, title:str, price:int, cat:Category):
        """
        Товар
        :param title: Наименование товара
        :param price: Цена товара
        :param cat: Категория товара
        """
        self.title = title
        self.price = price
        self.cat = cat
        Item.count += 1
        self.id = Item.count
