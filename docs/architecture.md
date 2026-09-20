# System Architecture

## Student Management System Architecture

```mermaid
flowchart TD

    A[User] --> B[Main Program<br/>main.py]

    B --> C[StudentManager<br/>Business Logic]

    C --> D[Validators<br/>Input Validation]
    C --> E[Models<br/>Student Class]
    C --> F[Reports<br/>Student Reports]

    E --> G[Storage<br/>JSON File Handling]

    G --> H[students.json<br/>Student Data]
```

## Architecture Components

| Component | Responsibility |
|---|---|
| Main Program | Provides the menu and handles user input |
| StudentManager | Handles student management operations |
| Models | Defines the Student class |
| Validators | Validates user input |
| Storage | Loads and saves student data |
| Reports | Generates basic student reports |
| students.json | Stores student records permanently |