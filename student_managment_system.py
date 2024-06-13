# Dictionary to store student records
students = {}


def add_student(name, age, grade, subjects):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """

    try:
        if name in students.keys():
            raise Exception("Student name already exist!")
        else:
            students[name] = {
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects
            }
            print("Student added!")
    except Exception as inst:
        print(inst)


def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """

    try:
        if name in students.keys():
            while True:
                try:
                    name = input("Enter updated student's name: ")
                    age = int(input("Enter updated student's age: "))
                    grade = float(input("Enter updated student's grade: "))
                    subjects = input("Enter updated student's subjects (comma-separated): ").split(", ")
                    updated_student = {"name": name, "age": age, "grade": grade, "subject": subjects}
                    students[name].update(updated_student)
                    break
                except ValueError:
                    print("Ops, please enter valid values. Try again...")
        else:
            raise Exception("Student not found. Try again...")
    except Exception as inst:
        print(inst)


def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    # Check if the student exists
    # Code to delete the student's record


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    # Check if the student exists
    # Code to return the student's record


def list_all_students():
    """
    List all student records.
    """
    # Check if there are any student records
    # Code to list all students
    try:
        if len(students) != 0:
            for key, value in students.items():
                print(key)
                for k, v in value.items():
                    print(f"\t{k}: {v}")
    except Exception as inst:
        print(inst)


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(', ')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()