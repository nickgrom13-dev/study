"""Разработать программную систему на основе принципов объектно-ориентированного
программирования (ООП), которая моделирует структуру
университета, факультетов и студентов, а также предоставляет функционал для
управления студентами."""

from University import University
from Faculty import Faculty
from Student import Student
from additional_functions import get_id

university_MGU = University("МГУ", [])

while 1:
    command = input("Выберите пункт меню:\n"
                    "1) Получить список всех студентов\n"
                    "2) Добавить факультет\n"
                    "3) Найти факультет по наименованию\n"
                    "4) Добавить студента на факультет\n"
                    "5) Удалить студента с факультета\n"
                    "6) Перевести студента на новый факультет\n"
                    "7) Найти студента по идентификатору\n"
                    "8) Выход\n").strip()

    match command:
        case "1":
            if not university_MGU.is_empty_faculties():
                students = university_MGU.get_all_students()
                if len(students) > 0:
                    print(f'В университете "{university_MGU.university_name}" '
                          f'обучаются следующие студенты:\n')
                    for i, student in enumerate(students, 1):
                        print(f"{i}) {student.get_student_info()}\n")
                else:
                    print(f'В университете "{university_MGU.university_name}" отсутствуют студенты.\n')
        case "2":
            faculty_name = input("Введите название факультета\n").strip().capitalize()
            if len(faculty_name) > 1:
                university_MGU.add_faculty(Faculty(faculty_name, []))
            else:
                print("Введено пустое значение\n")
        case "3":
            if not university_MGU.is_empty_faculties():
                faculty_name = input("Введите название факультета\n").strip().capitalize()
                faculty = university_MGU.get_faculty_by_name(faculty_name)
                if faculty:
                    faculty.show_faculty_info()
        case "4":
            if not university_MGU.is_empty_faculties():
                student_name = input("Введите ФИО студента\n").strip().title()
                faculty_name = input("Введите название факультета\n").strip().capitalize()
                if len(student_name) > 1 and len(faculty_name) > 1:
                    faculty = university_MGU.get_faculty_by_name(faculty_name)
                    if faculty:
                        faculty.add_student(Student(student_name, faculty))
                else:
                    print("Введено пустое значение\n")
        case "5":
            if not university_MGU.is_empty_faculties():
                student_id = get_id("студента", "удалить")
                if student_id != -1:
                    is_found_student = False
                    for faculty in university_MGU.faculties:
                        student = faculty.get_student_by_id(student_id)
                        if student:
                            is_found_student = True
                            faculty.remove_student(student)
                            break
                    if not is_found_student:
                        print(f'Студент с ID {student_id} не найден\n')
        case "6":
            if not university_MGU.is_empty_faculties():
                student_id = get_id("студента", "перевести")
                if student_id != -1:
                    is_found_student = False
                    for faculty in university_MGU.faculties:
                        student = faculty.get_student_by_id(student_id)
                        if student:
                            is_found_student = True
                            faculty_name = input("Введите название нового факультета\n").capitalize()
                            new_faculty = university_MGU.get_faculty_by_name(faculty_name)
                            if new_faculty:
                                student.transfer_to(new_faculty)
                            break
                    if not is_found_student:
                        print(f'Студент с ID {student_id} не найден\n')
        case "7":
            if not university_MGU.is_empty_faculties():
                student_id = get_id("студента", "найти")
                if student_id != -1:
                    is_found_student = False
                    for faculty in university_MGU.faculties:
                        student = faculty.get_student_by_id(student_id)
                        if student:
                            is_found_student = True
                            print(student.get_student_info())
                            break
                    if not is_found_student:
                        print(f'Студент с ID {student_id} не найден\n')
        case "8":
            break
        case _:
            print(f'Введен несуществующий пункт меню "{command}"\n')
