import re
from socket import *
from mypy.checkstrformat import Match

class CalculatorServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def start_server(self):
        """Запускает сервер"""
        try:
            server_socket = socket(AF_INET, SOCK_STREAM)
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"Сервер запущен на {self.host}:{self.port}")
            print("Ожидание подключений...")
            while True:
                client_socket, address = server_socket.accept()
                self.client_interaction(client_socket, address)
        except Exception as e:
            print(f"Ошибка сервера: {e}")

    def client_interaction(self, client_socket:socket, address):
        """
        Обрабатывает взаимодействие с клиентом
        :param client_socket: сокет для взаимодействия с клиентом
        :param address: адрес запроса
        :return:
        """
        print(f"Подключен клиент: {address}")
        try:
            while True:
                task = client_socket.recv(1024).decode('utf-8')
                if not task:
                    break
                print(f"Получено от {address}: {task}")
                if task.lower() == 'stop':
                    break
                result = self.calculate_task(task)
                client_socket.send(result.encode('utf-8'))
        except Exception as e:
            print(f"Ошибка при работе с клиентом {address}: {e}")
        client_socket.close()
        print(f"Соединение с клиентом {address} закрыто")


    def calculate_task(self, task:str)->str:
        """
        Вычисление математического примера
        :param task: пример, который нужно вычислить
        :return: результат вычисления
        """
        try:
            checked_task = self.check_task_format(task)
            if checked_task:
                a = float(checked_task.group(1))
                operator = checked_task.group(2)
                b = float(checked_task.group(3))
                result = 0
                match operator:
                    case '+':
                        result = a + b
                    case '-':
                        result = a - b
                    case '*':
                        result = a * b
                    case '/':
                        result = a / b
                    case _:
                        result = "Ошибка: указан неверный оператор"
                result = int(result) if result.is_integer() else round(result, 2)
                return str(result)
            return "Ошибка: Введенный пример не соответствует шаблону: a [+-*/] b"
        except ZeroDivisionError:
            return "Ошибка: Деление на ноль"
        except Exception as e:
            return f"Ошибка: {str(e)}"

    @staticmethod
    def check_task_format(task: str) -> Match|None:
        """
        Проверка введенного примера на соответствие шаблону
        :param task: Строка с примером, которую нужно проверить на соответствие шаблону
        :return: если пример соответствует шаблону, то возвращается соответствие регулярному выражению,
            иначе возвращается None
        """
        task_rule = re.compile(r'^\s*(-?\d+\.?\d*)\s*([\+\-\*\/])\s*(-?\d+\.?\d*)\s*$')
        match_rule = re.match(task_rule, task)
        if match_rule:
            return match_rule

if __name__ == "__main__":
    client = CalculatorServer('localhost', 8888)
    client.start_server()
