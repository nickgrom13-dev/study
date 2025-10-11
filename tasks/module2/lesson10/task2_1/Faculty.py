
"""
Модуль Faculty определяет класс Faculty для управления информацией о факультетах.

Класс Faculty предоставляет функциональность для:
- Добавления студента на факультет
- Удаления студента с факультета
- Возвращения студента по его идентификатору (ID)
- Вывода информации по факультету
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Student import Student

class Faculty:
    next_id = 0
    """Класс Факультет"""
    def __init__(self, faculty_name, students:list['Student']):
        Faculty.next_id += 1
        self.faculty_id = Faculty.next_id
        self.faculty_name = faculty_name
        self.students = students

    def add_student(self, student:'Student')->None:
        """
        Добавляет студента на факультет.
        :param student: Студент, которого нужно добавить, объект класса Student.
        """
        self.students.append(student)
        print(f'Студент {student.fullname} (ID: {student.student_id}) '
              f'добавлен на факультет "{self.faculty_name}"\n')

    def remove_student(self, student:'Student')->None:
        """
        Удаляет студента с факультета.
        :param student: Студент, которого нужно удалить, объект класса Student.
        """
        if student in self.students:
            self.students.remove(student)
            print(f'Студент {student.fullname} (ID: {student.student_id}) '
                  f'удален с факультета "{self.faculty_name}"\n')

    def get_student_by_id(self, student_id:int)->'Student|None':
        """
        Возвращает студента по его ID(или null, если не найден).
        :param student_id: Идентификатор студента, которого нужно найти.
        :return: Найденный студент, объект класса Student, или None в случае, если студент не найден.
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def show_faculty_info(self)->None:
        """
        Выводит информацию по факультету.
        """
        if len(self.students) > 0:
            print(f'В факультете "{self.faculty_name}" (ID: {self.faculty_id}) '
                  f'обучаются следующие студенты:\n')
            for i, student in enumerate(self.students, 1):
                print(f"{i}) {student.get_student_info()}\n")
        else:
            print(f'В факультете "{self.faculty_name}" (ID: {self.faculty_id}) нет студентов:\n')
