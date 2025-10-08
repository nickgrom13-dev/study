"""Создайте список с названиями шести школьных предметов.
Спросите у пользователя, какие из этих предметов ему не нравятся.
Удалите выбранные предметы из списка и выведите его повторно"""

def show_subjects(subjects:list)->None:
    """Вывод списка школьных предметов"""
    print(f"Список школьных предметов: {", ".join(subjects)}")

school_subjects = ["русский язык", "математика", "история", "география", "физика", "химия"]
show_subjects(school_subjects)

disliked_subjects = input("Какие предметы из представленных вам не нравятся? "
                          "Перечислите их через запятую.\n").lower().split(",")

for d_subject in disliked_subjects:
    d_subject = d_subject.strip()
    if d_subject in school_subjects:
        school_subjects.remove(d_subject)
    else:
        print(f'предмет "{d_subject}" не был указан в первоначальном списке')
show_subjects(school_subjects)
