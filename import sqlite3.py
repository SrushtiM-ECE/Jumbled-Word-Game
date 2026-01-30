import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks INTEGER
)
""")

conn.commit()


def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                   (id, name, course, marks))
    conn.commit()
    print("Student Added Successfully")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nID   Name    Course    Marks")
    print("-----------------------------")
    for row in rows:
        print(row)


def update_marks():
    sid = int(input("Enter student ID: "))
    new_marks = int(input("Enter new marks: "))

    cursor.execute("UPDATE students SET marks=? WHERE id=?",
                   (new_marks, sid))
    conn.commit()
    print("Marks Updated")


def delete_student():
    sid = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    print("Student Deleted")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you")
        break
    else:
        print("Invalid choice")

conn.close()
