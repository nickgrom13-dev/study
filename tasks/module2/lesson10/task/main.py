"""Разработать программную систему на основе принципов объектно-ориентированного
программирования (ООП), которая моделирует структуру
университета, факультетов и студентов, а также предоставляет функционал для
управления студентами."""
from University import University
from Faculty import Faculty
from Student import Student



university_1 = University("Югорский государственный университет", [])

while 1:
    command = input("Выберите пункт меню:\n"
                    "1) Получить список всех студентов\n"
                    "2) Добавить факультет\n"
                    "3) Найти факультет по наименованию\n"
                    "4) Добавить студента на факультет\n"
                    "5) Удалить студента с факультета\n"
                    "6) Найти студента по ID\n"
                    "7) Перевести студента на новый факультет\n"
                    "8) Вывести информацию по студенту\n"
                    "9) Выход\n")

    match command:
        case "1":
            students = university_1.get_all_students()
            if len(students) > 0:
                print(f'В университете "{university_1.university_name}" обучаются следующие студенты:\n')
                for i, student in enumerate(students, 1):
                    print(f"{i}) {student.get_student_info()}\n")
            else:
                print(f'В университете "{university_1.university_name}" отсутствуют студенты.\n')
        case "2":
            faculty_name = input("Введите название факультета\n").capitalize()
            university_1.add_faculty(Faculty(university_1.get_next_faculty_id(), faculty_name, []))
        case "3":
            faculty_name = input("Введите название факультета\n").capitalize()
            faculty = university_1.get_faculty_by_name(faculty_name)
            if isinstance(faculty, Faculty):
                faculty.show_faculty_info()
        case "4":
            student_name = input("Введите ФИО студента\n").title()
            faculty_name = input("Введите название факультета\n").capitalize()
            faculty = university_1.get_faculty_by_name(faculty_name)
            if isinstance(faculty, Faculty):
                faculty.add_student(Student(university_1.get_next_student_id(), student_name, faculty))
        case "5":
                student_id = input('Введите ID студента, которого нужно удалить\n')
                try:
                    student_id = int(student_id)
                    students = university_1.get_all_students()
                    for student in students:
                        if student.student_id == student_id:
                            student.faculty.remove_student(student)
                            break
                except ValueError:
                    print(f"Введено некорректное значение ID: {student_id}\n")
        case "6":
            found_student = None
            student_id = input('Введите ID студента, которого нужно найти\n')
            try:
                student_id = int(student_id)
                students = university_1.get_all_students()
                for student in students:
                    if student.student_id == student_id:
                        found_student = student.faculty.get_student_by_id(student_id)
                        break
                if isinstance(found_student, Student):
                    print(found_student.get_student_info())
            except ValueError:
                print(f"Введено некорректное значение ID: {student_id}\n")
        case "7":
            found_student = None
            student_id = input('Введите ID студента, которого нужно перевести\n')
            try:
                student_id = int(student_id)
                students = university_1.get_all_students()
                for student in students:
                    if student.student_id == student_id:
                        found_student = student.faculty.get_student_by_id(student_id)
                        break
                if isinstance(found_student, Student):
                    faculty_name = input("Введите название факультета\n").capitalize()
                    faculty = university_1.get_faculty_by_name(faculty_name)
                    if isinstance(faculty, Faculty):
                        found_student.transfer_to(faculty)
            except ValueError:
                print(f"Введено некорректное значение ID: {student_id}\n")
        case "8":
            found_student = None
            student_id = input('Введите ID студента, которого нужно найти\n')
            try:
                student_id = int(student_id)
                students = university_1.get_all_students()
                for student in students:
                    if student.student_id == student_id:
                        found_student = student.faculty.get_student_by_id(student_id)
                        break
                if isinstance(found_student, Student):
                    print(found_student.get_student_info())
            except ValueError:
                print(f"Введено некорректное значение ID: {student_id}\n")
        case "9":
            break
        case _:
            print(f'Введен несуществующий пункт меню "{command}"\n')