"""
Класс AdminPanel определяет работу админа в админской панели
"""
from AdminOperation import AdminOperation

class AdminPanel:
    def __init__(self):
        """
        Панель администратора
        """
        self.__admins = [
            {"login": "admin", "pass": "123"},
            {"login": "admin2", "pass": "456"},
            {"login": "admin3", "pass": "789"}
        ]
        self.__admin_operation = AdminOperation()
        self.__admin_operation.fill_admin_operation()
        self.__catalog = self.__admin_operation.catalog

    def get_catalog(self):
        """
        Геттер для получения каталога товаров
        :return:
        """
        return self.__catalog

    def authorization_admin(self):
        """
        Проверяем, является ли пользователь админом
        """
        login = input("Введите логин:\n")
        password = input("Введите пароль:\n")
        find_admin = {"login": login, "pass": password}
        if find_admin in self.__admins:
            self.__show_admin_panel()
        else:
            print("Ошибка авторизации. Пользователя с указанными логином и паролем не существует.")

    def __show_admin_panel(self):
        """
        Показать панель администратора
        """
        while True:
            command = input("\n=== Панель администратора ===\n"
                            "1) Показать каталог товаров\n"
                            "2) Добавить товар в каталог\n"
                            "3) Удалить товар из каталога\n"
                            "4) Обновить цену товара\n"
                            "0) Выйти\n").strip()

            match command:
                case "1":
                    self.__catalog.show_items()
                case "2":
                    self.__admin_operation.add_item_to_catalog()
                case "3":
                    self.__admin_operation.remove_item_from_catalog()
                case "4":
                    self.__admin_operation.update_item_price()
                case "0":
                    break
                case _:
                    print(f"Введена неверная команда: {command}")
