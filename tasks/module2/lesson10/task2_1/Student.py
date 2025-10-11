
"""
Модуль Student определяет класс Student для управления информацией о студентах.

Класс Student предоставляет функциональность для:
- Возвращения строки с полной информацией о студенте (ID, ФИО, название факультета)
- Перевода студента на новый факультет
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Faculty import Faculty

class Student:
    next_id = 0
    """Класс Студент"""
    def __init__(self, fullname:str, faculty:'Faculty'):
        Student.next_id += 1
        self.student_id = Student.next_id
        self.fullname = fullname
        self.faculty = faculty

    def get_student_info(self)->str:
        """
        Возвращает строку с полной информацией о студенте.
        :return: Строку, в которой содержится информация о студенте.
        """
        return (f'Студент {self.fullname} (ID: {self.student_id}) '
                f'находится на факультете "{self.faculty.faculty_name}"')

    def transfer_to(self, new_faculty:'Faculty')->None:
        """
        Переводит студента на новый факультет.
        :param new_faculty: Факультет, на который нужно перевести студента, объект класса Faculty.
        """
        old_faculty = self.faculty
        old_faculty.remove_student(self)
        self.faculty = new_faculty
        self.faculty.add_student(self)

        print(f'Студент {self.fullname} (ID: {self.student_id}) '
              f'переведен из факультета "{old_faculty.faculty_name}"'
              f' в факультет "{new_faculty.faculty_name}"\n')
