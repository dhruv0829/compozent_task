
students = {}


def create_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades = input("Enter student grades (comma-separated): ").split(',')
    
    students[student_id] = {"name": name, "age": age, "grades": grades}
    print("Student created successfully!")


def read_student():
    student_id = input("Enter student ID to view: ")
    
    if student_id in students:
        student = students[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grades: {', '.join(student['grades'])}")
    else:
        print("ID not found!")


def update_student():
    student_id = input("Enter student ID to update: ")
    
    if student_id in students:
        name = input("Enter new student name: ")
        age = int(input("Enter new student age: "))
        grades = input("Enter new student grades (comma-separated): ").split(',')
        
        students[student_id] = {"name": name, "age": age, "grades": grades}
        print("Student ID updated successfully!")
    else:
        print("ID not found!")


def delete_student():
    student_id = input("Enter student ID to delete: ")
    
    if student_id in students:
        del students[student_id]
        print("Student ID deleted successfully!")
    else:
        print("ID not found!")


def display_menu():
    print("\nStudent Data Management")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


while True:       
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_student()
    elif choice == '2':
        read_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
