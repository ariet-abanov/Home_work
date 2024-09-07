class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "married" if self.is_married else "not married"
        return f"Name: {self.fullname}, Age: {self.age}, Marital Status: {marital_status}"

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        if self.marks:
            total_marks = sum(self.marks.values())
            subjects_count = len(self.marks)
            return total_marks / subjects_count
        return 0

    def introduce_myself(self):
        student_info = super().introduce_myself()
        marks_info = ', '.join([f"{subject}: {mark}" for subject, mark in self.marks.items()])
        return f"{student_info}, Marks: {marks_info}"

class Teacher(Person):
    base_salary = 30000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = 0.05 * bonus_years * self.base_salary
            return self.base_salary + bonus
        return self.base_salary

    def introduce_myself(self):
        teacher_info = super().introduce_myself()
        return f"{teacher_info}, Experience: {self.experience} years, Salary: {self.calculate_salary()}"

def create_students():
     student1 = Student("Atai", 14, False, {"Math": 5, "History": 4, "Biology": 3})
     student2 = Student("Agahan", 14, False, {"Math": 5, "History": 4, "Biology": 3})
     student3 = Student("Ariet", 14, False, {"Math": 5, "History": 4, "Biology": 4})
     return [student1, student2, student3]

students = create_students()
for student in students:
    print(student.introduce_myself())
    print(f"Average Mark: {student.calculate_average_mark()}")

teacher = Teacher("Tariel agai", 28, True, 4)
print(teacher.introduce_myself())