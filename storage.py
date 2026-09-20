import json
import os


def load_students():
    if os.path.exists("students.json"):
        try:
            with open("students.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    return []


def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)