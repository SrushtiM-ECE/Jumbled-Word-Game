# Student Marks Manager

students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\nStudent List:")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} - {s['marks']}")
    print()

def average_marks():
    if not students:
        print("No data to calculate average.\n")
        return

    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    print(f"Average Marks: {avg:.2f}\n")

def topper():
    if not students:
        print("No students found.\n")
        return

    top = max(students, key=lambda x: x["marks"])
    print(f"Topper: {top['name']} with {top['marks']} marks\n")

while True:
    print("==== Student Marks Manager ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Average Marks")
    print("4. Show Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        average_marks()
    elif choice == "4":
        topper()
    elif choice == "5":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Try again.\n")
