import random

print("=== Number Guessing Game ===")
print("I am thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
import random

print("=== Number Guessing Game ===")
print("I am thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
