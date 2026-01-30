print("Welcome to Simple Quiz App")

name = input("Enter your name: ")

score = 0

print("\nAnswer the following questions:")

# Question 1
print("\n1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Chennai")

ans1 = input("Your answer: ")

if ans1.lower() == "b":
    score += 1

# Question 2
print("\n2. Which language is used for Data Science?")
print("a) Python")
print("b) HTML")
print("c) CSS")

ans2 = input("Your answer: ")

if ans2.lower() == "a":
    score += 1

# Question 3
print("\n3. What is 10 + 20?")
print("a) 20")
print("b) 25")
print("c) 30")

ans3 = input("Your answer: ")

if ans3.lower() == "c":
    score += 1

print("\nQuiz Finished")
print("Name:", name)
print("Your Score:", score, "/3")

if score == 3:
    print("Excellent")
elif score == 2:
    print("Good")
else:
    print("Keep practicing")
