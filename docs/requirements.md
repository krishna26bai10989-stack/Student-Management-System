# Project Requirements

## 1. Functional Requirements

Functional requirements describe what the Student Management System should be able to do.

### 1. Add Student

The system should allow the user to enter:

- Student name
- Roll number
- Course

Before adding the record, the system checks that the required details are not empty and that the roll number is not already present.

### 2. View Students

The system should display all the student records currently stored in the system.

### 3. Search Student

The system should allow the user to search for a student using the roll number.

If the roll number is found, the student's details are displayed. Otherwise, the system shows a student-not-found message.

### 4. Update Student

The system should allow the user to update the name and course of an existing student.

The student is selected using the roll number.

### 5. Delete Student

The system should allow the user to delete an existing student record using the roll number.

### 6. Student Report

The system should generate a basic report containing:

- Total number of students
- Number of students in each course

### 7. Data Storage

The system should save student records in `students.json` and load the saved records when the application starts.

### 8. Input Validation

The system should check user input and prevent empty name, roll number and course fields.

It should also prevent duplicate roll numbers.

---

## 2. Non-Functional Requirements

Non-functional requirements describe how the system should behave.

### 1. Usability

The application should have a simple menu so that a user can understand and operate it without complicated instructions.

### 2. Reliability

Student records should be saved after changes so that the information is available when the program is started again.

### 3. Error Handling

The system should handle common problems such as:

- Empty input
- Duplicate roll number
- Student not found
- Invalid JSON data
- Invalid menu choice

### 4. Maintainability

The project is divided into separate Python files such as `models.py`, `storage.py`, `validators.py`, `student_manager.py` and `reports.py`.

This makes individual parts of the program easier to understand and modify.

### 5. Performance

The system should perform normal student operations such as searching, adding, updating and deleting without unnecessary processing.

Since the project is designed for a small number of student records, JSON storage is sufficient for the current scope.

### 6. Scalability

The project structure allows additional features to be added later, such as student attendance, marks, login functionality or a graphical interface.

### 7. Resource Efficiency

The application uses a lightweight JSON file instead of requiring a separate database server, keeping the project simple and lightweight.

---

## 3. Summary

The functional requirements define the operations provided by the Student Management System, while the non-functional requirements focus on usability, reliability, error handling, maintainability, performance, scalability and resource efficiency.