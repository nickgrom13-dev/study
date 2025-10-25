import re
from socket import *

class CalculatorClient:
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port

    def connect_to_server(self)->socket|None:
        """
        Подключение к серверу
        :return: если подключение прошло успешно, то возвращает сокет для взаимодействия с сервером,
            иначе возвращает None
        """
        try:
            client_socket = socket(AF_INET, SOCK_STREAM)
            client_socket.connect((self.host, self.port))
            return client_socket
        except Exception as e:
            print(f"Ошибка при подключении к серверу: {e}")

    def request_calculation(self):
        """Отправка запроса на вычисление математического примера"""
        client_socket = self.connect_to_server()
        if client_socket:
            print("Подключение к серверу установлено.\n"
                  "Введите примеры для решения (например, a + b, a * b, a / b, "
                  "где a и b - числа).\n"
                  "Для выхода введите команду stop.")
            while True:
                task = input("Введите пример для вычисления:\n").strip()
                if not task:
                    print("Ошибка: Пустой ввод")
                    continue
                if task.lower() == "stop":
                    client_socket.send('stop'.encode('utf-8'))
                    print("Завершение работы программы.")
                    break
                try:
                    task = self.clean_task(task)
                    client_socket.send(task.encode('utf-8'))
                    response = client_socket.recv(1024).decode('utf-8')

                    if response.find("Ошибка") != -1:
                        print(response)
                    else:
                        print(f"{task} = {response}")
                    print('-' * 50)
                except Exception as e:
                    print(f"Ошибка при обмене данными с сервером: {e}")
                    break
            client_socket.close()

    @staticmethod
    def clean_task(task:str)->str:
        """
        Очистить в примере лишние пробелы
        :param task: Строка с примером
        :return: Очищенная строка с примером
        """
        # Убираем все пробелы
        no_spaces = re.sub(r'\s+', '', task)

        # Добавляем пробелы вокруг операторов (кроме минуса в отрицательных числах)
        # Сначала обрабатываем операторы +, *, /
        cleaned = re.sub(r'([\+\*\/])', r' \1 ', no_spaces)

        # Затем обрабатываем оператор - только если он не часть отрицательного числа
        cleaned = re.sub(r'(?<!\d)\s*-\s*(\d)', r' -\1', cleaned)
        cleaned = re.sub(r'(\d)\s*-\s*', r'\1 - ', cleaned)

        return cleaned.strip()

if __name__ == "__main__":
    client = CalculatorClient('localhost', 8888)
    client.request_calculation()
