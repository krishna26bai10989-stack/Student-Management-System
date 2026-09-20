import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from student_manager import StudentManager


def test_add_student():
    manager = StudentManager()

    success, message = manager.add_student(
        "Test Student",
        "TEST001",
        "CSE AIML"
    )

    assert success is True
    assert message == "Student added successfully!"

    manager.delete_student("TEST001")


def test_search_student():
    manager = StudentManager()

    manager.add_student(
        "Test Student",
        "TEST002",
        "CSE AIML"
    )

    student = manager.search_student("TEST002")

    assert student is not None
    assert student.name == "Test Student"

    manager.delete_student("TEST002")


def test_delete_student():
    manager = StudentManager()

    manager.add_student(
        "Test Student",
        "TEST003",
        "CSE AIML"
    )

    success, message = manager.delete_student("TEST003")

    assert success is True
    assert message == "Student deleted successfully!"

    assert manager.search_student("TEST003") is None


def test_update_student():
    manager = StudentManager()

    manager.add_student(
        "Old Name",
        "TEST004",
        "CSE AIML"
    )

    success, message = manager.update_student(
        "TEST004",
        "New Name",
        "CSE"
    )

    assert success is True
    assert message == "Student updated successfully!"

    student = manager.search_student("TEST004")

    assert student is not None
    assert student.name == "New Name"
    assert student.course == "CSE"

    manager.delete_student("TEST004")


def test_duplicate_roll_number():
    manager = StudentManager()

    manager.add_student(
        "First Student",
        "TEST005",
        "CSE AIML"
    )

    success, message = manager.add_student(
        "Second Student",
        "TEST005",
        "CSE"
    )

    assert success is False
    assert message == "Roll number already exists."

    manager.delete_student("TEST005")


def test_empty_name():
    manager = StudentManager()

    success, message = manager.add_student(
        "",
        "TEST006",
        "CSE AIML"
    )

    assert success is False
    assert message == "Name cannot be empty."

    assert manager.search_student("TEST006") is None