def show_report(students):

    print("\n================================")
    print("       STUDENT REPORT")
    print("================================")

    if len(students) == 0:
        print("No students available.")
        return

    print("Total Students:", len(students))

    courses = {}

    for student in students:

        if student.course in courses:
            courses[student.course] += 1
        else:
            courses[student.course] = 1

    print("\nStudents by Course:")

    for course, count in courses.items():
        print(course, ":", count)

    print("================================")