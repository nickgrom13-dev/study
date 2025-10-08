class Faculty:
    def __init__(self, faculty_id, faculty_name, students:list['Student']):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.students = students

    def add_student(self, student:'Student')->None:
        """Добавляет студента на факультет"""
        self.students.append(student)
        print(f'Студент {student.fullname} (ID: {student.student_id}) добавлен на факультет "{self.faculty_name}"\n')

    def remove_student(self, student:'Student')->None:
        """Удаляет студента с факультета"""
        if student in self.students:
            self.students.remove(student)
            print(f'Студент {student.fullname} (ID: {student.student_id}) удален с факультета "{self.faculty_name}"\n')

    def get_student_by_id(self, student_id:int)->'Student|None':
        """Возвращает студента по его ID(или null, если не найден)"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        print(f"Студент с ID {student_id} не найден на факультете\n")
        return None

    def show_faculty_info(self)->None:
        """Выводит информацию по факультету"""
        if len(self.students) > 0:
            print(f'В факультете "{self.faculty_name}" (ID: {self.faculty_id}) обучаются следующие студенты:\n')
            for i, student in enumerate(self.students, 1):
                print(f"{i}) {student.get_student_info()}\n")
        else:
            print(f'В факультете "{self.faculty_name}" (ID: {self.faculty_id}) нет студентов:\n')