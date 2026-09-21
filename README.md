Student Management System

1. Project Overview

The Student Management System is a simple Python project made to manage student records.

In this project, a user can add, view, search, update and delete student details. The project also stores the student data in a JSON file, so the data is available even after closing the program.

I made this project using basic Python concepts like functions, classes, loops, conditions, file handling and exception handling.

2. Main Features

The project has the following features:

Add a new student

View all students

Search a student using roll number

Update student details

Delete a student

Generate a student report

Store student data in a JSON file

Prevent duplicate roll numbers

Check for empty input

Handle common errors

3. Technologies Used

Python 3 - Used to develop the project

JSON - Used to store student data

pytest - Used for testing the project

VS Code - Used for writing and running the code

Git - Used for version control

GitHub - Used to store the project online

4. Project Structure

The project is divided into different files so that the code is easy to understand and manage.


Student Management System/
│
├── main.py
├── models.py
├── storage.py
├── validators.py
├── student_manager.py
├── reports.py
├── students.json
│
├── tests/
│   └── test_student_manager.py
│
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── use_case.md
│   ├── class_diagram.md
│   ├── sequence_diagram.md
│   ├── data_storage.md
│   └── requirements.md
│
├── README.md
├── statement.md
└── .gitignore



File Details

File

Work

main.py

Runs the main program and shows the menu

models.py

Contains the Student class

storage.py

Loads and saves student data

validators.py

Checks whether student details are valid

student_manager.py

Handles add, search, update and delete operations

reports.py

Creates the student report

students.json

Stores student records

tests/

Contains automated tests

docs/

Contains project design and documentation

statement.md

Contains the problem statement and project scope

.gitignore

Keeps unnecessary files out of Git

5. Main Menu

When the program is started, the following menu is displayed:

   STUDENT MANAGEMENT SYSTEM

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Report
7. Exit

The user selects an option from 1 to 7 and the program performs the selected operation.

6. How to Run the Project

Step 1: Install Python

Python 3 should be installed on the computer.

To check Python, run:

python --version

Step 2: Open the Project Folder

Open the project folder in VS Code.

Step 3: Run the Application

Open the terminal in the project folder and run:

python main.py

The Student Management System menu will appear.

7. How to Run Tests

The project uses pytest for automated testing.

If pytest is not installed, install it using:

python -m pip install pytest

Then run:

python -m pytest

The current project has 6 automated tests, and all 6 tests are passing.

Example result:

6 passed

8. Data Storage

The student records are stored in:

students.json

A student record contains:

{
    "name": "Krishna Sharma",
    "roll": "10989",
    "course": "CSE AI/ML"
}

When the program starts, it loads the saved student records.

When a student is added, updated or deleted, the changes are saved in the JSON file.

9. Validation and Error Handling

The project checks the entered information before saving it.

For example:

Student name cannot be empty.

Roll number cannot be empty.

Course cannot be empty.

Duplicate roll numbers are not allowed.

If a student is not found, the program shows an appropriate message.

Invalid or corrupted JSON data is handled by the storage module.

Invalid menu choices are handled by the main program.

10. Testing

I created automated tests using pytest to check the important functions of the project.

The tests check:

Adding a student

Searching for a student

Deleting a student

Updating a student

Duplicate roll number

Empty student name

All 6 tests are passing.

11. Documentation

The docs folder contains the design and project documentation.

It includes:

System architecture

Project workflow

Use case diagram

Class diagram

Sequence diagram

Data storage design

Functional and non-functional requirements

12. What I Learned From This Project

While making this project, I learned:

How to create a Python project using multiple files

How classes and objects work

How to use functions and loops

How to work with JSON files

How to validate user input

How to handle errors

How to create CRUD operations

How to write automated tests using pytest

How to use Git and GitHub

How to organize project documentation

13. Future Improvements

In the future, this project can be improved by adding:

Graphical User Interface (GUI)

Web-based interface

Login system

Student attendance

Marks and grades

Database such as MySQL or SQLite

Export reports to PDF or CSV

Admin dashboard

14. Conclusion

The Student Management System is a simple project that helps manage student records in an organized way.

This project helped me understand how Python can be used to build a complete application instead of writing only small programs.

The project also gave me practical experience with modular programming, JSON storage, CRUD operations, validation, testing, Git and GitHub.
