"""
Модуль UserInterface содержит класс UserInterface.
"""
from UserManagement import UserManagement
from PasswordValidator import PasswordValidator

class UserInterface:
    """
    Класс для взаимодействия пользователя с программой.
    """
    def __init__(self):
        data_file = "users.json"
        self.user_manager = UserManagement(data_file)
        self.password_validator = PasswordValidator()

    @staticmethod
    def input_username()->str:
        """
        Ввод имени пользователя
        :return: имя пользователя
        """
        while True:
            username = input("Введите имя пользователя: \n").strip()
            if not username:
                print("Имя пользователя не может быть пустым.")
                continue
            if ' ' in username:
                print("Имя пользователя не может содержать пробелы.")
                continue
            break
        return username

    def add_user(self):
        """Добавить нового пользователя"""
        print("\n--- ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ ---")

        username = self.input_username()

        if self.user_manager.is_user_exists(username):
            print(f"Пользователь с именем {username} уже существует. Пожалуйста, выберите другое.")
            return

        self.password_validator.display_password_requirements()
        password = self.password_validator.input_password()

        if self.user_manager.append_user(username, password):
            print(f"Пользователь '{username}' успешно добавлен.")
        else:
            print(f"Ошибка при добавлении пользователя {username}.")

    def change_password(self):
        """Изменить пароль у пользователя"""
        print("\n--- ИЗМЕНЕНИЕ ПАРОЛЯ ---")

        username = self.input_username()

        if not self.user_manager.is_user_exists(username):
            print(f"Пользователь с именем {username} не найден.")
            return

        print(f"Изменение пароля для пользователя: {username}")
        self.password_validator.display_password_requirements()
        new_password = self.password_validator.input_password()

        if self.user_manager.update_password(username, new_password):
            print(f"Пароль для пользователя '{username}' успешно изменен.")
        else:
            print(f"Ошибка при изменении пароля для пользователя {username}.")

    def show_users(self):
        """Вывести список пользователей"""
        print("\n--- СПИСОК ПОЛЬЗОВАТЕЛЕЙ ---")

        usernames = self.user_manager.get_all_usernames()

        if not usernames:
            print("Список пользователей пуст")
            return

        print(f"Всего пользователей: {len(usernames)}")
        print("-" * 30)
        for i, username in enumerate(usernames, 1):
            print(f"{i}) {username}")
        print("-" * 30)
