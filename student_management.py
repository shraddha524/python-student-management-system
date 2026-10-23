
students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks (out of 100): "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll_no']}")
        print(f"Marks: {student['marks']}")
        print("-" * 25)

def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            return

    print("Student not found.")

def calculate_average():
    if not students:
        print("No student records available.")
        return

    average = sum(s["marks"] for s in students) / len(students)
    print(f"Average marks: {average:.2f}")

def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
