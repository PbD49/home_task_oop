class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def calculate_average_grade_student(self, students, course):
        grades = []
        for student in students:
            if course in student.grades:
                grades += student.grades[course]
        if grades:
            average_grade = sum(grades) / len(grades)
            return average_grade
        else:
            return 0


    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: "
                f"{self.calculate_average_grade_student([self], 'Python')}\nКурсы в процессе изучения: "
                f"{', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")


    def __lt__(self, other):
        return self.calculate_average_grade_student([self], 'Python') < other.calculate_average_grade_student([other],
                                                                                                              'Python')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def calculate_average_lecture_grade(self, lecturers, course):
        grades = []
        for lecturer in lecturers:
            if course in lecturer.grades:
                grades += lecturer.grades[course]
        if grades:
            average_grade = sum(grades) / len(grades)
            return average_grade
        else:
            return 0


    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: "
                f"{self.calculate_average_lecture_grade([self], 'Python')}")


    def __lt__(self, other):
        return self.calculate_average_lecture_grade([self], 'Python') < other.calculate_average_lecture_grade([other],
                                                                                                              'Python')

best_student = Student('Aleksey', 'Mukhin', 'men')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']


cool_student = Student('Ivan', 'Abramov', 'men')
cool_student.courses_in_progress += ['Python', 'Git']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


cool_mentor.rate_student(best_student, 'Python', 9.9)
cool_mentor.rate_student(best_student, 'Git', 9.9)


cool_mentor.rate_student(cool_student, 'Python', 9.7)
cool_mentor.rate_student(cool_student, 'Git', 10)


first_lecturer = Lecturer('Some', 'Buddy')
first_lecturer.courses_attached += ['Python', 'Git']
second_lecturer = Lecturer('Dmitriy', 'Petrosyan')
second_lecturer.courses_attached += ['Python', 'Git']


cool_student.rate_lecturer(first_lecturer, 'Python', 10)
cool_student.rate_lecturer(first_lecturer, 'Git', 10)


best_student.rate_lecturer(second_lecturer, 'Python', 9.9)
best_student.rate_lecturer(second_lecturer, 'Git', 9.9)


print(cool_mentor)
print(second_lecturer)
print(best_student)


print(best_student > cool_student)
print(first_lecturer < second_lecturer)