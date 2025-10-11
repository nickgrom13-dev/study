"""
Модуль Currency определяет класс Currency для управления информацией о валютах.
"""
class Currency:
    def __init__(self, code:str, name:str):
        self.code = code
        self.name = name
    def __str__(self):
        return f"{self.name} ({self.code})"
