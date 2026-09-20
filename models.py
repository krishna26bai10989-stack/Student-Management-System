class Student:

    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Course:", self.course)