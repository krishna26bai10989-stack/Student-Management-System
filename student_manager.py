from models import Student
from storage import load_students, save_students
from validators import validate_name, validate_roll, validate_course


class StudentManager:

    def __init__(self):
        self.students = []

        data = load_students()

        for student in data:
            obj = Student(
                student["name"],
                student["roll"],
                student["course"]
            )
            self.students.append(obj)

    def add_student(self, name, roll, course):

        if not validate_name(name):
            return False, "Name cannot be empty."

        if not validate_roll(roll):
            return False, "Roll number cannot be empty."

        if not validate_course(course):
            return False, "Course cannot be empty."

        if self.search_student(roll) is not None:
            return False, "Roll number already exists."

        student = Student(name, roll, course)
        self.students.append(student)

        self.save_data()

        return True, "Student added successfully!"

    def get_students(self):
        return self.students

    def search_student(self, roll):

        for student in self.students:

            if student.roll == roll:
                return student

        return None

    def update_student(self, roll, name, course):

        student = self.search_student(roll)

        if student is None:
            return False, "Student not found."

        if not validate_name(name):
            return False, "Name cannot be empty."

        if not validate_course(course):
            return False, "Course cannot be empty."

        student.name = name
        student.course = course

        self.save_data()

        return True, "Student updated successfully!"

    def delete_student(self, roll):

        student = self.search_student(roll)

        if student is None:
            return False, "Student not found."

        self.students.remove(student)

        self.save_data()

        return True, "Student deleted successfully!"

    def save_data(self):

        data = []

        for student in self.students:

            data.append({
                "name": student.name,
                "roll": student.roll,
                "course": student.course
            })

        save_students(data)