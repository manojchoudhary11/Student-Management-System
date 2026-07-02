"""
Student Management System
A beginner-friendly Python application to manage student records.

Features:
- Add student
- View students
- Search student
- Update student
- Delete student
- Save/load data using JSON
"""

import json
import os
from datetime import datetime

DATA_FILE = "students.json"


def load_data():
    """Load student data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ Data file is corrupted. Starting with empty records.")
        return []
    except Exception as error:
        print(f"✗ Error loading data: {error}")
        return []


def save_data(students):
    """Save student data to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        print("✓ Data saved successfully!")
    except Exception as error:
        print(f"✗ Error saving data: {error}")


def validate_student_id(student_id, students):
    """Validate student ID."""
    if not student_id.strip():
        print("✗ Student ID cannot be empty!")
        return False

    for student in students:
        if student["id"].lower() == student_id.lower():
            print("✗ Student ID already exists!")
            return False

    return True


def validate_name(name):
    """Validate student name."""
    if not name.strip():
        print("✗ Name cannot be empty!")
        return False

    if not name.replace(" ", "").isalpha():
        print("✗ Name should contain only letters and spaces!")
        return False

    return True


def validate_age(age):
    """Validate student age."""
    try:
        age_number = int(age)

        if age_number < 1 or age_number > 120:
            print("✗ Age must be between 1 and 120!")
            return False

        return True
    except ValueError:
        print("✗ Age must be a number!")
        return False


def validate_email(email):
    """Validate email address."""
    if not email.strip():
        print("✗ Email cannot be empty!")
        return False

    if "@" not in email or "." not in email:
        print("✗ Please enter a valid email address!")
        return False

    return True


def validate_phone(phone):
    """Validate phone number."""
    cleaned_phone = (
        phone.replace("-", "")
        .replace(" ", "")
        .replace("(", "")
        .replace(")", "")
    )

    if not cleaned_phone.isdigit():
        print("✗ Phone number should contain only digits!")
        return False

    if len(cleaned_phone) < 10:
        print("✗ Phone number must contain at least 10 digits!")
        return False

    return True


def add_student(students):
    """Add a new student."""
    print("\n" + "=" * 50)
    print("ADD NEW STUDENT")
    print("=" * 50)

    while True:
        student_id = input("Enter Student ID: ").strip()
        if validate_student_id(student_id, students):
            break

    while True:
        name = input("Enter Name: ").strip()
        if validate_name(name):
            break

    while True:
        age = input("Enter Age: ").strip()
        if validate_age(age):
            break

    course = input("Enter Course: ").strip()

    while True:
        email = input("Enter Email: ").strip()
        if validate_email(email):
            break

    while True:
        phone = input("Enter Phone Number: ").strip()
        if validate_phone(phone):
            break

    student = {
        "id": student_id,
        "name": name,
        "age": int(age),
        "course": course,
        "email": email,
        "phone": phone,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    students.append(student)
    save_data(students)

    print(f"\n✓ Student '{name}' added successfully!")


def view_students(students):
    """View all students."""
    print("\n" + "=" * 120)
    print("ALL STUDENTS")
    print("=" * 120)

    if not students:
        print("No students found. Add a student first!")
        return

    print(
        f"{'ID':<8} | {'Name':<20} | {'Age':<5} | "
        f"{'Course':<20} | {'Email':<30} | {'Phone':<15}"
    )
    print("-" * 120)

    for student in students:
        print(
            f"{student['id']:<8} | {student['name']:<20} | "
            f"{student['age']:<5} | {student['course']:<20} | "
            f"{student['email']:<30} | {student['phone']:<15}"
        )

    print("=" * 120)
    print(f"Total Students: {len(students)}")


def search_student(students):
    """Search student by ID."""
    print("\n" + "=" * 50)
    print("SEARCH STUDENT")
    print("=" * 50)

    search_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"].lower() == search_id.lower():
            print("\n✓ Student Found!")
            print("-" * 40)
            print(f"ID:         {student['id']}")
            print(f"Name:       {student['name']}")
            print(f"Age:        {student['age']}")
            print(f"Course:     {student['course']}")
            print(f"Email:      {student['email']}")
            print(f"Phone:      {student['phone']}")
            print(f"Date Added: {student['date_added']}")
            print("-" * 40)
            return

    print(f"\n✗ No student found with ID '{search_id}'")


def update_student(students):
    """Update student details."""
    print("\n" + "=" * 50)
    print("UPDATE STUDENT")
    print("=" * 50)

    search_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"].lower() == search_id.lower():
            print(f"\n✓ Found student: {student['name']}")

            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            print("4. Email")
            print("5. Phone")
            print("6. Cancel")

            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == "1":
                while True:
                    new_name = input("Enter new Name: ").strip()
                    if validate_name(new_name):
                        student["name"] = new_name
                        break

            elif choice == "2":
                while True:
                    new_age = input("Enter new Age: ").strip()
                    if validate_age(new_age):
                        student["age"] = int(new_age)
                        break

            elif choice == "3":
                student["course"] = input("Enter new Course: ").strip()

            elif choice == "4":
                while True:
                    new_email = input("Enter new Email: ").strip()
                    if validate_email(new_email):
                        student["email"] = new_email
                        break

            elif choice == "5":
                while True:
                    new_phone = input("Enter new Phone Number: ").strip()
                    if validate_phone(new_phone):
                        student["phone"] = new_phone
                        break

            elif choice == "6":
                print("Update cancelled.")
                return

            else:
                print("✗ Invalid choice!")
                return

            save_data(students)
            print(f"\n✓ Student '{student['name']}' updated successfully!")
            return

    print(f"✗ No student found with ID '{search_id}'")


def delete_student(students):
    """Delete student record."""
    print("\n" + "=" * 50)
    print("DELETE STUDENT")
    print("=" * 50)

    search_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student["id"].lower() == search_id.lower():
            print(f"\n⚠️ Are you sure you want to delete '{student['name']}'?")
            confirm = input("Type 'yes' to confirm: ").strip().lower()

            if confirm == "yes":
                students.remove(student)
                save_data(students)
                print(f"\n✓ Student '{student['name']}' deleted successfully!")
            else:
                print("Delete cancelled.")

            return

    print(f"✗ No student found with ID '{search_id}'")


def display_menu():
    """Display main menu."""
    print("\n" + "=" * 50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 50)


def main():
    """Main program function."""
    students = load_data()

    if students:
        print(f"\n✓ Loaded {len(students)} student(s) from {DATA_FILE}")
    else:
        print("\n✓ Starting with empty database")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("\n" + "=" * 50)
            print("Thank you for using Student Management System!")
            print("=" * 50)
            break
        else:
            print("✗ Invalid choice! Please enter a number between 1 and 6.")

        if choice != "6":
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()