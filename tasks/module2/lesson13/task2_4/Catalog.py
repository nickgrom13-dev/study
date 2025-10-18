"""
Класс Cart определяет свойства и методы каталога товаров
"""
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Cart import Cart
from ItemCart import ItemCart
from Store import Store
from Item import Item

class Catalog(Store):
    def __init__(self, items:list[Item]):
        """
        Список товаров в каталоге
        :param items: список товаров для каталога
        """
        self.items = items

    def show_items(self):
        """
        Вывести список товаров из каталога
        """
        print(f"{'ID товара':^12} {'Название товара':^20} "
              f"{'Стоимость товара':^18} {'Категория товара':^15}")
        for item in self.items:
            print(f"{item.id:^12} {item.title:^20} "
                  f"{item.price:^18} {item.cat.title:^15}")

    def get_item(self, id_item:int)->Item|None:
        """
        Поиск товара по ID.
        :param id_item: ID товара
        :return: Товар, который найден по ID
        """
        for item in self.items:
            if item.id == id_item:
                return item
        print(f"Товар c ID {id_item} не найден")
        return None

    def add_item_to_cart(self, cart:'Cart'):
        """
        Добавление товара в корзину
        :param cart: Корзина товаров
        """
        try:
            id_item = int(input('Введите ID товара, который добавляем в корзину\n'))
            item_for_cart = self.get_item(id_item) #Получили товар для корзины
            if item_for_cart:
                item_cart = ItemCart(id_item)
                cart.save_item_in_cart(item_cart, True)
                print(f"Товар '{item_for_cart.title}' добавлен в корзину!")
        except ValueError:
            print("Пожалуйста, введите корректный ID товара (число)")

    def remove_item_from_cart(self, cart:'Cart'):
        """
        Удаление товара из корзины
        :param cart: Корзина товаров
        """
        try:
            id_item = int(input('Введите ID товара, который удаляем из корзины\n'))
            item_for_cart = self.get_item(id_item) #Получили товар для корзины
            if item_for_cart:
                item_cart = ItemCart(id_item)
                cart.save_item_in_cart(item_cart, False)
                print(f"Товар '{item_for_cart.title}' удален из корзины!")
        except ValueError:
            print("Пожалуйста, введите корректный ID товара (число)")
