import json
import os

# -----------------------------
# Student Class
# -----------------------------
class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }

# -----------------------------
# Student Manager Class
# -----------------------------
class StudentManager:
    FILE_NAME = "students.json"

    def __init__(self):
        self.students = []
        self.load_data()

    # Load students from file
    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.students = [Student(**s) for s in data]
        else:
            self.students = []

    # Save students to file
    def save_data(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump([s.to_dict() for s in self.students], file, indent=4)

    # Add student
    def add_student(self):
        try:
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            student = Student(student_id, name, age, course, marks)
            self.students.append(student)
            self.save_data()

            print("✅ Student added successfully!\n")

        except ValueError:
            print("❌ Invalid input. Please enter correct values.\n")

    # View all students
    def view_students(self):
        if not self.students:
            print("No students found.\n")
            return

        print("\n--- Student List ---")
        for s in self.students:
            print(f"ID: {s.student_id}, Name: {s.name}, Age: {s.age}, Course: {s.course}, Marks: {s.marks}")
        print()

    # Search student
    def search_student(self):
        sid = input("Enter Student ID to search: ")
        found = False

        for s in self.students:
            if s.student_id == sid:
                print("\nStudent Found:")
                print(f"ID: {s.student_id}")
                print(f"Name: {s.name}")
                print(f"Age: {s.age}")
                print(f"Course: {s.course}")
                print(f"Marks: {s.marks}\n")
                found = True
                break

        if not found:
            print("❌ Student not found.\n")

    # Update student
    def update_student(self):
        sid = input("Enter Student ID to update: ")

        for s in self.students:
            if s.student_id == sid:
                print("Leave blank to keep old value.")
                name = input(f"New Name ({s.name}): ") or s.name
                age_input = input(f"New Age ({s.age}): ")
                course = input(f"New Course ({s.course}): ") or s.course
                marks_input = input(f"New Marks ({s.marks}): ")

                s.name = name
                s.age = int(age_input) if age_input else s.age
                s.course = course
                s.marks = float(marks_input) if marks_input else s.marks

                self.save_data()
                print("✅ Student updated successfully!\n")
                return

        print("❌ Student not found.\n")

    # Delete student
    def delete_student(self):
        sid = input("Enter Student ID to delete: ")

        for s in self.students:
            if s.student_id == sid:
                self.students.remove(s)
                self.save_data()
                print("🗑️ Student deleted successfully!\n")
                return

        print("❌ Student not found.\n")

    # Show statistics
    def show_statistics(self):
        if not self.students:
            print("No data available.\n")
            return

        marks_list = [s.marks for s in self.students]

        avg_marks = sum(marks_list) / len(marks_list)
        highest = max(marks_list)
        lowest = min(marks_list)

        print("\n--- Statistics ---")
        print(f"Total Students : {len(self.students)}")
        print(f"Average Marks  : {avg_marks:.2f}")
        print(f"Highest Marks  : {highest}")
        print(f"Lowest Marks   : {lowest}\n")

# -----------------------------
# Main Menu
# -----------------------------
def main():
    manager = StudentManager()

    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Statistics")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            manager.show_statistics()
        elif choice == "7":
            print("Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    main()
