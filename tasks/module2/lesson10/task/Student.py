class Student:
    def __init__(self, student_id:int, fullname:str, faculty:'Faculty'):
        self.student_id = student_id
        self.fullname = fullname
        self.faculty = faculty

    def get_student_info(self)->str:
        """Возвращает строку с полной информацией о студенте"""
        return f'Студент {self.fullname} (ID: {self.student_id}) находится в факультете "{self.faculty.faculty_name}"'

    def transfer_to(self, new_faculty:'Faculty')->None:
        """Переводит студента на новый факультет"""
        old_faculty = self.faculty
        old_faculty.remove_student(self)
        self.faculty = new_faculty
        self.faculty.add_student(self)

        print(f'Студент {self.fullname} (ID: {self.student_id}) переведен из факультета "{old_faculty}"'
              f' в факультет "{new_faculty}"\n')

