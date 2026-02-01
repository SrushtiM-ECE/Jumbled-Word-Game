# Student Marks Analyzer

name = input("Enter student name: ")

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / n

# Grade logic
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Result
result = "Pass" if average >= 40 else "Fail"

print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Status:", result)
