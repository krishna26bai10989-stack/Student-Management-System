from student_manager import StudentManager
from reports import show_report


manager = StudentManager()


while True:

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # ADD STUDENT
    if choice == "1":

        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        course = input("Enter Course: ")

        success, message = manager.add_student(
            name,
            roll,
            course
        )

        print(message)


    # VIEW STUDENTS
    elif choice == "2":

        students = manager.get_students()

        if len(students) == 0:

            print("No students found.")

        else:

            print("\n===== STUDENTS =====")

            for student in students:

                print("Name:", student.name)
                print("Roll:", student.roll)
                print("Course:", student.course)

                print("--------------------")


    # SEARCH STUDENT
    elif choice == "3":

        roll = input("Enter Roll No to search: ")

        student = manager.search_student(roll)

        if student is not None:

            print("\nStudent Found!")

            print("Name:", student.name)
            print("Roll:", student.roll)
            print("Course:", student.course)

        else:

            print("Student not found.")


    # UPDATE STUDENT
    elif choice == "4":

        roll = input("Enter Roll No to update: ")

        student = manager.search_student(roll)

        if student is not None:

            print("\nStudent Found!")

            new_name = input("Enter new name: ")
            new_course = input("Enter new course: ")

            success, message = manager.update_student(
                roll,
                new_name,
                new_course
            )

            print(message)

        else:

            print("Student not found.")


    # DELETE STUDENT
    elif choice == "5":

        roll = input("Enter Roll No to delete: ")

        success, message = manager.delete_student(roll)

        print(message)


    # REPORT
    elif choice == "6":

        students = manager.get_students()

        show_report(students)


    # EXIT
    elif choice == "7":

        print("Thank You!")
        print("Exiting Student Management System...")

        break


    else:

        print("Invalid choice! Please try again.")
        