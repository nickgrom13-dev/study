"""
Класс Category определяет свойства категории товаров
"""
class Category:
    count = 0

    def __init__(self, title_cat:str):
        """
        :param title_cat:Наименование категории
        """
        self.title = title_cat
        Category.count += 1
        self.id = Category.count
    def __str__(self):
        return f"{self.id:^12} {self.title:^20}"
