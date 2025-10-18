"""
Класс ItemCart определяет свойства товара в корзине
"""
class ItemCart:

    def __init__(self, id_item:int):
        """
        :param id_item: ID товара
        """
        self.quantity = 1
        self.id = id_item
