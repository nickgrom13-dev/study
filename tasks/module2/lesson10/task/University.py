class University:
    def __init__(self, university_name:str, faculties:list['Faculty']):
        self.university_name = university_name
        self.faculties = faculties

    def add_faculty(self, faculty: 'Faculty')->None:
        """Добавляет факультет в университет"""
        for item in self.faculties:
            if item.faculty_name == faculty.faculty_name:
                print(f'В университете "{self.university_name}" уже есть факультет с наименованием "{faculty.faculty_name}"\n')
                return
        self.faculties.append(faculty)
        print(f'В университет "{self.university_name}" добавлен факультет с наименованием "{faculty.faculty_name}"\n')

    def get_faculty_by_name(self, faculty_name: str)->'Faculty|None':
        """Возвращает факультет по названию"""
        for faculty in self.faculties:
            if faculty.faculty_name == faculty_name:
                return faculty
        print(f'В университете "{self.university_name}" нет факультета с наименованием "{faculty_name}"\n')
        return None

    def get_all_students(self)->list['Student']:
        """Возвращает список всех студентов университета (со всех факультетов)"""
        students = []
        for faculty in self.faculties:
                students += faculty.students
        return students

    def get_next_faculty_id(self)->int:
        """Получает следующий индекс для ID факультета"""
        ids = [0]
        for faculty in self.faculties:
            ids.append(faculty.faculty_id)
        return max(ids) + 1

    def get_next_student_id(self)->int:
        """Получает следующий индекс для ID студента"""
        ids = [0]
        for faculty in self.faculties:
            for student in faculty.students:
                ids.append(student.student_id)
        return max(ids) + 1