"""
Модуль UserManagement содержит класс UserManagement.
"""
import json
import os.path

class UserManagement:
    """
    Класс для управления пользователями.
    """
    def __init__(self, data_file:str):
        self.data_file = data_file
        self.users = []
        self.load_users()

    def load_users(self)->None:
        """Загружает список пользователей из файла"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.users = json.load(f)  # конвертируем json файл в словарь
            except Exception as e:
                print(f"Ошибка при загрузке файла {self.data_file}: {e}")

    def save_users(self) -> None:
        """Сохраняет пользователей в файл"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def is_user_exists(self, username: str) -> bool:
        """
        Проверяет существование пользователя в списке пользователей
        :param username: имя пользователя, наличие которого нужно проверить
        :return: True - если пользователь уже есть в списке, иначе False
        """
        usernames = list(map(lambda item: item['username'], self.users))
        return username in usernames

    def append_user(self, username: str, password: str) -> bool:
        """
        Добавляет нового пользователя в список
        :param username: имя нового пользователя
        :param password: пароль нового пользователя
        :return: True - если пользователя добавлен в список, иначе False
        """
        if self.is_user_exists(username):
            return False
        self.users.append({"username":username, "password":password})
        self.save_users()
        return True

    def update_password(self, username: str, new_password: str) -> bool:
        """
        Обновляет пароль пользователя
        :param username: пользователь, которому нужно обновить пароль
        :param new_password: новый пароль
        :return: True - если пароль обновлен, иначе False
        """
        if not self.is_user_exists(username):
            return False
        for user in self.users:
            if user['username'] == username:
                user['password'] = new_password
                break
        self.save_users()
        return True

    def get_all_usernames(self) -> list[str]:
        """
        Получить список всех пользователей
        :return: список всех имен пользователей
        """
        return list(map(lambda item: item['username'], self.users))
