"""
Класс Cart определяет свойства и методы корзины покупок
"""
from Store import Store
from Catalog import Catalog
from ItemCart import ItemCart

class Cart(Store):

    def __init__(self):
        """
        Корзина покупок
        """
        self.items_cart = []

    def show_items(self, catalog:Catalog=None):
        """
        Вывести список товаров из корзины
        :param catalog: Каталог товаров
        """
        if not catalog:
            print("Не был передан параметр catalog (каталог товаров)")
            return None
        print(f"{'ID товара':<12} {'Название товара':<20} {'Стоимость товара':<18} "
              f"{'Количество':<12} {'Общая стоимость':<15}")
        for item in self.items_cart:
            advanced_item = catalog.get_item(item.id)
            if advanced_item:
                total_cost = advanced_item.price * item.quantity
                print(f"{item.id:<12} {advanced_item.title:<20} {advanced_item.price:<18} "
                      f"{item.quantity:<12} {total_cost:<15}")
        return None

    def save_item_in_cart(self, new_item:ItemCart, is_add:bool):
        """
        В этом методе работаем со свойством количество:
        либо добавим/удалим данное свойство, либо увеличим/уменьшим на 1
        :param new_item: Новый товар для корзины
        :param is_add: Если True, то добавляем товар, иначе удаляем товар
        """
        if not new_item:
            print("Не был передан параметр new_item (новый товар в корзину)")
            return None
        for item in self.items_cart:
            #Если добавляемый товар уже есть в корзине
            if item.id == new_item.id:
                if is_add:
                    item.quantity += 1
                else:
                    item.quantity -= 1
                    if item.quantity == 0:
                        self.items_cart.remove(item)
                break
        else:
           if is_add:
            self.items_cart.append(new_item)
        return None

    def clear_cart(self):
        """
        Очистка корзины
        """
        self.items_cart.clear()
        print("Корзина очищена")
