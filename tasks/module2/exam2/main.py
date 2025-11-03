"""
Напишите программу, которая сохраняет логины пользователей и их пароли.
"""
from UserInterface import UserInterface

def main():
    """Основная функция программы"""
    user_interface = UserInterface()
    while True:
        print("\n" + "=" * 50)
        print("      СИСТЕМА УПРАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯМИ")
        print("=" * 50)

        command = input("Меню:\n"
                        "1) Добавить пользователя\n"
                        "2) Изменить пароль у пользователя\n"
                        "3) Вывести список пользователей\n"
                        "4) Выход\n").strip()
        match command:
            case "1":
                user_interface.add_user()
            case "2":
                user_interface.change_password()
            case "3":
                user_interface.show_users()
            case "4":
                break
            case _:
                print(f"Введена неверная команда: {command}\n")

if __name__ == "__main__":
    main()
