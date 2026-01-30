def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


print("===== Student Marks Analyzer =====")

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i+1}")

    name = input("Enter student name: ")

    m1 = float(input("Enter marks 1: "))
    m2 = float(input("Enter marks 2: "))
    m3 = float(input("Enter marks 3: "))

    total = m1 + m2 + m3
    average = total / 3

    grade = calculate_grade(average)

    print("\n--- Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

print("\nProgram finished.")
