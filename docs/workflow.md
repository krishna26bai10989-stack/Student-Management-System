# Student Management System - Workflow

## Program Flow

The program starts by displaying the Student Management System menu. 
The user selects one of the available options from 1 to 7.

```mermaid
flowchart TD

    START([Start]) --> MENU[Display Main Menu]

    MENU --> CHOICE{Enter Choice}

    CHOICE -->|1| ADD[Add Student]
    ADD --> ADD_INPUT[Enter Name, Roll No and Course]
    ADD_INPUT --> VALIDATE[Validate Student Details]
    VALIDATE --> DUPLICATE{Roll Number Already Exists?}
    DUPLICATE -->|Yes| ERROR1[Show Error Message]
    DUPLICATE -->|No| SAVE1[Save Student]
    SAVE1 --> SUCCESS1[Show Success Message]
    ERROR1 --> MENU
    SUCCESS1 --> MENU

    CHOICE -->|2| VIEW[View Students]
    VIEW --> SHOW[Display All Student Records]
    SHOW --> MENU

    CHOICE -->|3| SEARCH[Search Student]
    SEARCH --> SEARCH_INPUT[Enter Roll Number]
    SEARCH_INPUT --> FIND[Search Student Record]
    FIND --> FOUND{Student Found?}
    FOUND -->|Yes| DISPLAY[Display Student Details]
    FOUND -->|No| ERROR2[Show Student Not Found]
    DISPLAY --> MENU
    ERROR2 --> MENU

    CHOICE -->|4| UPDATE[Update Student]
    UPDATE --> UPDATE_INPUT[Enter Roll Number]
    UPDATE_INPUT --> FIND2[Find Student Record]
    FIND2 --> FOUND2{Student Found?}
    FOUND2 -->|Yes| NEW_DETAILS[Enter New Name and Course]
    NEW_DETAILS --> VALIDATE2[Validate Details]
    VALIDATE2 --> SAVE2[Update and Save Student]
    SAVE2 --> SUCCESS2[Show Success Message]
    FOUND2 -->|No| ERROR3[Show Student Not Found]
    SUCCESS2 --> MENU
    ERROR3 --> MENU

    CHOICE -->|5| DELETE[Delete Student]
    DELETE --> DELETE_INPUT[Enter Roll Number]
    DELETE_INPUT --> FIND3[Find Student Record]
    FIND3 --> FOUND3{Student Found?}
    FOUND3 -->|Yes| REMOVE[Delete Student]
    REMOVE --> SAVE3[Save Updated Data]
    SAVE3 --> SUCCESS3[Show Success Message]
    FOUND3 -->|No| ERROR4[Show Student Not Found]
    SUCCESS3 --> MENU
    ERROR4 --> MENU

    CHOICE -->|6| REPORT[Student Report]
    REPORT --> REPORT_DATA[Get Student Records]
    REPORT_DATA --> REPORT_RESULT[Calculate Total and Course-wise Count]
    REPORT_RESULT --> DISPLAY_REPORT[Display Student Report]
    DISPLAY_REPORT --> MENU

    CHOICE -->|7| EXIT([Exit Program])
```

## Menu Options

| Option | Operation | What it does |
|---|---|---|
| 1 | Add Student | Adds a new student record |
| 2 | View Students | Shows all saved student records |
| 3 | Search Student | Searches for a student using roll number |
| 4 | Update Student | Changes the name or course of an existing student |
| 5 | Delete Student | Removes a student record |
| 6 | Student Report | Shows total students and course-wise count |
| 7 | Exit | Closes the program |

## How the Workflow Works

1. The program starts and displays the main menu.
2. The user selects an option from **1 to 7**.
3. The selected operation is performed.
4. Required student information is validated.
5. Changes are saved in `students.json` where required.
6. The result is shown to the user.
7. After completing an operation, the program returns to the main menu.
8. When the user selects **7**, the program exits.

## Main Modules Used

```text
main.py
   ↓
student_manager.py
   ↓
├── models.py
├── validators.py
├── storage.py
└── reports.py
   ↓
students.json
```

These modules divide the work of the project into smaller parts and make the program easier to understand and maintain.