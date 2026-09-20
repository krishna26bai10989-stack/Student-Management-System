# Data Storage Design

## Storage Method

The Student Management System uses a JSON file named `students.json` to store student records.

JSON was selected because the project is a small Python-based application and JSON is simple to read, write and manage using Python.

## Student Record Structure

Each student record contains three fields:

| Field | Description | Example |
|---|---|---|
| `name` | Name of the student | `Rahul Sharma` |
| `roll` | Unique roll number of the student | `24CSE001` |
| `course` | Student's course | `CSE AIML` |

## Example of `students.json`

```json
[
    {
        "name": "Rahul Sharma",
        "roll": "24CSE001",
        "course": "CSE AIML"
    },
    {
        "name": "Aman Verma",
        "roll": "24CSE002",
        "course": "CSE AIML"
    }
]
```

## Data Flow

```text
Student Details
      ↓
main.py
      ↓
StudentManager
      ↓
Validation
      ↓
storage.py
      ↓
students.json
```

When the application starts, `storage.py` reads the saved records from `students.json`.

When a student is added, updated or deleted, the updated records are written back to the same JSON file.

## Data Operations

| Operation | Storage Action |
|---|---|
| Add Student | Adds a new record to `students.json` |
| View Students | Reads records from the JSON file |
| Search Student | Searches the loaded student records |
| Update Student | Changes an existing record and saves it |
| Delete Student | Removes a record and saves the changes |
| Student Report | Uses the stored student records to generate a report |

## Data Validation

Before adding or updating a student, the system checks that:

- Name is not empty.
- Roll number is not empty.
- Course is not empty.
- Roll number is not already used when adding a student.

The storage module also handles invalid JSON data by returning an empty list instead of stopping the application.

## Why JSON?

JSON is suitable for this project because:

- It is easy to understand.
- It works directly with Python.
- It does not require a separate database server.
- Student records can be stored permanently.
- It is simple to edit and inspect during development.