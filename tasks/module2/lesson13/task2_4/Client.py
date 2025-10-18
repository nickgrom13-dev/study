"""
Класс Client определяет работу клиента с магазином
"""
from Cart import Cart
from AdminPanel import AdminPanel

class Client:

    @staticmethod
    def show_main_menu(admin_panel):
        """
        Показать меню магазина
        """
        catalog = admin_panel.get_catalog()
        cart = Cart()
        while True:
            command = input("\n=== МЕНЮ ===\n"
                            "1) Показать каталог товаров\n"
                            "2) Добавить товар в корзину\n"
                            "3) Удалить товар из корзины\n"
                            "4) Показать корзину товаров\n"
                            "5) Очистить корзину товаров\n"
                            "6) Зайти в меню администратора\n"
                            "0) Выйти\n").strip()

            match command:
                case "1":
                    catalog.show_items()
                case "2":
                    catalog.add_item_to_cart(cart)
                case "3":
                    catalog.remove_item_from_cart(cart)
                case "4":
                    cart.show_items(catalog)
                case "5":
                    cart.clear_cart()
                case "6":
                    admin_panel.authorization_admin()
                case "0":
                    break
                case _:
                    print(f"Введена неверная команда: {command}\n")

    def run(self):
        """Запуск приложения"""
        print("Магазин автомобилей")
        self.show_main_menu(AdminPanel())
