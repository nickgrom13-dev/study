"""
Модуль PasswordValidator содержит класс PasswordValidator.
"""
import re

class PasswordValidator:
    """Класс для проверки (валидации) паролей"""

    SPECIAL_CHARS = '!£$%&'

    @staticmethod
    def display_password_requirements() -> None:
        """Отображает требования к паролю"""
        print("\nТребования к паролю:")
        print("- Не менее 8 символов")
        print("- Буквы верхнего регистра")
        print("- Буквы нижнего регистра")
        print("- Цифры")
        print(f"- Специальные символы: {PasswordValidator.SPECIAL_CHARS}")

    @staticmethod
    def is_value_contains_chars(value: str, chars: str) -> bool:
        """
        Проверяет передаваемое значение на наличие указанных символов
        :param value: проверяемое значение (строка)
        :param chars: символы, которые проверяются на наличие в значении
        :return: True - если строка содержит указанные символы, иначе False
        """
        for char in value:
            if char in chars:
                return True
        return False

    @staticmethod
    def check_password_strength(password: str) -> tuple[int, list[str]]:
        """
        Проверяет силу пароля и возвращает баллы и сообщения
        :param password: проверяемый пароль
        :return: баллы надежности пароля и не соблюденные требования к сложности пароля
        """
        score = 0
        messages = []
        special_chars = PasswordValidator.SPECIAL_CHARS

        requirements = [
            (
                len(password) >= 8,
                "Пароль должен содержать не менее 8 символов"
            ),
            (
                re.search(r'[A-ZА-Я]', password),
                "Пароль должен включать буквы верхнего регистра"
            ),
            (
                re.search(r'[a-zа-я]', password),
                "Пароль должен включать буквы нижнего регистра"
            ),
            (
                re.search(r'\d', password),
                "Пароль должен включать цифры"
            ),
            (
                PasswordValidator.is_value_contains_chars(password, special_chars),
                f"Пароль должен включать хотя бы один специальный символ: {special_chars}"
            )
        ]

        for condition, message in requirements:
            if condition:
                score += 1
            else:
                messages.append(message)
        return score, messages

    @staticmethod
    def get_strength_status(score: int) -> str:
        """
        Возвращает статус надежности пароля
        :param score: баллы надежности пароля
        :return: статус надежности пароля
        """
        if score == 5:
            strength_status = "Пароль является сильным"
        elif score >= 3:
            strength_status = f"Пароль можно улучшить. Баллы: {score}/5"
        else:
            strength_status = f"Пароль слабый. Баллы: {score}/5"
        return strength_status

    @staticmethod
    def input_password() -> str:
        """
        Ввод пользователем валидного пароля
        :return: пароль, который удовлетворяет требованиям
        """
        while True:
            password = input("Введите пароль:\n").strip()
            score, messages = PasswordValidator.check_password_strength(password)
            strength_status = PasswordValidator.get_strength_status(score)

            print(strength_status)

            if score == 5:
                break

            if score >= 3:
                print("\nРекомендации по улучшению:")
                for item in messages:
                    print(f"  - {item}")

                try_again = input("\nХотите повторить попытку? (да/нет): \n").lower()
                if try_again in ['да', 'д', 'yes', 'y']:
                    continue
                break

            print("\nНеобходимые улучшения:")
            for item in messages:
                print(f"  - {item}")
            print("Пожалуйста, придумайте более надежный пароль.\n")
        return password
