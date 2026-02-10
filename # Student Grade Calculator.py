# Student Grade Calculator

name = input("Enter student name: ")
marks = []

for i in range(1, 6):
    score = float(input(f"Enter marks for subject {i}: "))
    marks.append(score)

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n--- Student Report ---")
print("Name:", name)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
