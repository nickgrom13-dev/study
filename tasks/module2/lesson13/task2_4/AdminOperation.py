"""
Класс AdminOperation определяет методы и свойства для админских операций
"""
from Category import Category
from Item import Item
from Catalog import Catalog

class AdminOperation:

    def __init__(self):
        """
        Операции администратора
        """
        self.categories = []
        self.catalog = None

    def init_primary_data(self):
        """
        Инициализация первичных данных
        :return: Каталог товаров
        """
        cat_rus = self.get_category_by_id(1)
        cat2_import = self.get_category_by_id(2)

        item1 = Item("ВАЗ", 1000, cat_rus)
        item2 = Item("УАЗ", 1200, cat_rus)
        item3 = Item("ГАЗ", 1300, cat_rus)

        item4 = Item("BMW", 5000, cat2_import)
        item5 = Item("KIA", 3000, cat2_import)
        item6 = Item("JAC", 4000, cat2_import)

        cars = [item1, item2, item3, item4, item5, item6]

        return Catalog(cars)

    @staticmethod
    def init_categories():
        """
        Инициализация категорий товаров
        :return: Список категорий товаров
        """
        cat1 = Category("Российские автомобили")
        cat2 = Category("Импортные автомобили")
        return [cat1, cat2]

    def fill_admin_operation(self):
        """
        Заполнение свойств класса операции админа
        :return:
        """
        self.categories = self.init_categories()
        self.catalog = self.init_primary_data()

    def get_category_by_id(self, id_category:int)->Category|None:
        """
        Поиск категории товара по ID.
        :param id_category: ID товара
        :return: Категория товара, которая найдена по ID
        """
        for category in self.categories:
            if category.id == id_category:
                return category
        print(f"Категория c ID {id_category} не найдена")
        return None

    def add_item_to_catalog(self):
        """
        Добавление товара в каталог
        """
        try:
            print(f"{'ID категории':^12} {'Название категории':^20} ")
            for category in self.categories:
                print(category)
            id_category = int(input("Выберите категорию товара из списка (укажите ID категории)\n").strip())
            category_for_add = self.get_category_by_id(id_category)
            if category_for_add:
                item_title = input("Введите название товара\n").strip().capitalize()
                item_price = int(input("Введите цену товара\n").strip())
                self.catalog.items.append(Item(item_title, item_price, category_for_add))
                print(f"Товар категории {category_for_add.title} с названием {item_title} "
                      f"и ценной {item_price} добавлен в каталог")
        except ValueError:
            print("Введено некорректное значение")
        except Exception as e:
            print(f"Другая ошибка ({type(e).__name__}): {e}")

    def remove_item_from_catalog(self):
        """
        Удаление товара из каталога
        """
        try:
            id_item = int(input('Введите ID товара, который нужно удалить из каталога\n'))
            item_to_del = self.catalog.get_item(id_item)
            if item_to_del:
                self.catalog.items.remove(item_to_del)
                print(f"Товар категории {item_to_del.cat.title} с названием {item_to_del.title} "
                      f"и ID {item_to_del.id} удален из каталога")
        except ValueError:
            print("Введено некорректное значение")
        except Exception as e:
            print(f"Другая ошибка ({type(e).__name__}): {e}")

    def update_item_price(self):
        """
        Обновление цены товара по ID
        :return:
        """
        try:
            id_item = int(input('Введите ID товара, у которого нужно обновить цену\n'))
            item_to_update = self.catalog.get_item(id_item)
            if item_to_update:
                new_price = int(input('Введите новую цену товара\n'))
                item_to_update.price = new_price
                print(f"У товара {item_to_update.title} ID ({item_to_update.id}) установлена новая цена {new_price}")
        except ValueError:
            print("Введено некорректное значение")
        except Exception as e:
            print(f"Другая ошибка ({type(e).__name__}): {e}")
