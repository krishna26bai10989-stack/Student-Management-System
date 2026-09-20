# Student Management System

## 1. Project Overview

The Student Management System is a Python-based command-line application developed to manage student records in a simple and organized way.

The system allows users to add, view, search, update and delete student information. It also provides a basic student report and stores records permanently using a JSON file.

The project is developed using a modular structure so that different parts of the application are separated into different Python files.

---

## 2. Features

The main features of the system are:

### Student Management
- Add a new student
- View all students
- Search a student using roll number
- Update student details
- Delete a student record

### Data Storage
- Stores student records in `students.json`
- Loads saved records when the application starts
- Automatically saves changes after add, update or delete operations

### Validation
- Prevents empty student name
- Prevents empty roll number
- Prevents empty course
- Prevents duplicate roll numbers

### Student Report
- Displays total number of students
- Displays course-wise student count

### Error Handling
- Handles student-not-found cases
- Handles duplicate roll numbers
- Handles invalid or corrupted JSON data
- Handles invalid menu choices

### Testing
- Automated testing using `pytest`
- Tests for adding students
- Tests for searching students
- Tests for updating students
- Tests for deleting students
- Tests for duplicate roll numbers
- Tests for empty student names

---

## 3. Technologies and Tools

The project uses the following technologies and tools:

- **Python 3** - Main programming language
- **JSON** - Student data storage
- **pytest** - Automated testing
- **Visual Studio Code** - Development environment
- **Git** - Version control
- **GitHub** - Project repository and version management

No external package is required to run the main application.

---

## 4. Project Structure

```text
Student Management System/
│
├── main.py
├── models.py
├── storage.py
├── validators.py
├── student_manager.py
├── reports.py
├── students.json
├── style.css
├── README.md
├── statement.md
│
├── tests/
│   └── test_student_manager.py
│
└── docs/
    ├── architecture.md
    ├── workflow.md
    ├── use_case.md
    ├── class_diagram.md
    ├── sequence_diagram.md
    ├── data_storage.md
    └── requirements.md

    Module Description
File	Purpose
main.py	Main program and menu
models.py	Contains the Student class
storage.py	Loads and saves JSON data
validators.py	Validates student information
student_manager.py	Handles student operations
reports.py	Generates student reports
students.json	Stores student records
test_student_manager.py	Automated tests
docs/	Project design and documentation
5. Main Menu

The application provides the following menu:

================================
     STUDENT MANAGEMENT SYSTEM
================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Report
7. Exit

The user selects an option and the system performs the corresponding operation.

6. Installation and Setup
Step 1: Install Python

Install Python 3.x on your computer.

Check the installation using:

python --version
Step 2: Open the Project

Open the project folder in Visual Studio Code.

Step 3: Install Testing Tool

The main application does not require external packages.

For running automated tests, install pytest:

python -m pip install pytest
7. How to Run the Project

Open the terminal inside the project folder and run:

python main.py

The Student Management System menu will appear.

Select an option from 1 to 7 to use the application.

8. Data Storage

Student records are stored in:

students.json

Each student record contains:

{
    "name": "Student Name",
    "roll": "ROLL001",
    "course": "CSE AIML"
}

The application automatically loads existing records when it starts.

Changes made through add, update and delete operations are saved to the JSON file.

9. Testing

The project uses pytest for automated testing.

Run the tests using:

python -m pytest

The current test suite checks:

Adding a student
Searching for a student
Deleting a student
Updating a student
Duplicate roll number validation
Empty name validation

The current version contains 6 automated tests.

10. Documentation

Detailed project documentation is available in the docs folder.

The documentation includes:

System architecture
Program workflow
Use case diagram
Class diagram
Sequence diagram
Data storage design
Functional and non-functional requirements

The project also contains:

statement.md - Problem statement, scope, target users and objectives
README.md - Project overview and setup information
11. Functional Requirements

The system supports the following major operations:

Create student records
Read/view student records
Search student records
Update student records
Delete student records
Generate basic student reports
Store records permanently

These operations form the main workflow of the application.

12. Non-Functional Requirements

The project considers the following non-functional requirements:

Usability - Simple menu-based interface
Reliability - Student data is saved after changes
Error Handling - Common input and data errors are handled
Maintainability - Code is divided into separate modules
Performance - Operations are designed for efficient handling of small student datasets
Scalability - The structure allows additional features to be added
Resource Efficiency - Uses lightweight JSON storage
13. Project Objective

The objective of this project is to develop a simple and modular Student Management System while applying Python programming concepts such as:

Functions
Classes and Objects
Lists
Loops
Conditional Statements
File Handling
JSON
Exception Handling
Modular Programming
Automated Testing
14. Future Enhancements

The project can be extended in the future with features such as:

Graphical User Interface
Web-based interface
Student login system
Attendance management
Marks and grade management
Database integration
Exporting student reports
Admin dashboard
15. Conclusion

The Student Management System provides a simple way to manage student records using Python.

The project demonstrates modular programming, CRUD operations, JSON-based data storage, input validation, error handling and automated testing.

The modular structure also provides a foundation for extending the application with more advanced student management features in the future.