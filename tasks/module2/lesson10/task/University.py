
"""
Модуль University определяет класс University для управления информацией об университете.

Класс University предоставляет функциональность для:
- Добавления факультета в университет
- Возвращения факультета по наименованию
- Возвращения списка всех студентов университета (со всех факультетов)
- Проверка на наличие факультетов в университете
"""

from Student import Student
from Faculty import Faculty

class University:
    """Класс Университет"""
    def __init__(self, university_name:str, faculties:list['Faculty']):
        self.university_name = university_name
        self.faculties = faculties

    def add_faculty(self, faculty: 'Faculty')->None:
        """
        Добавляет факультет в университет.
        :param faculty: Факультет, который нужно добавить, объект класса Faculty.
        """
        for item in self.faculties:
            if item.faculty_name == faculty.faculty_name:
                print(f'В университете "{self.university_name}" '
                      f'уже есть факультет с наименованием "{faculty.faculty_name}"\n')
                return
        self.faculties.append(faculty)
        print(f'В университет "{self.university_name}" добавлен '
              f'факультет с наименованием "{faculty.faculty_name}"\n')

    def get_faculty_by_name(self, faculty_name: str)->'Faculty|None':
        """
        Возвращает факультет по названию.
        :param faculty_name: Наименование факультета, который нужно найти.
        :return: Найденный факультет, объект класса Faculty, или None в случае, если факультет не найден.
        """
        for faculty in self.faculties:
            if faculty.faculty_name == faculty_name:
                return faculty
        print(f'В университете "{self.university_name}" '
              f'нет факультета с наименованием "{faculty_name}"\n')
        return None

    def get_all_students(self)->list['Student']:
        """
        Возвращает список всех студентов университета (со всех факультетов).
        :return: Возвращает список всех студентов университета.
        """
        students = []
        for faculty in self.faculties:
            students += faculty.students
        return students

    def is_empty_faculties(self)->bool:
        """
        Проверка на наличие факультетов в университете.
        :return: Возвращает True, если в университете нет факультетов, иначе возвращает False.
        """
        if len(self.faculties) > 0:
            return False
        else:
            print(f'В университете "{self.university_name}" отсутствуют факультеты.\n')
            return True
