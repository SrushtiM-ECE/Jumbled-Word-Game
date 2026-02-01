# Number Guessing Game

import random

print("=== Number Guessing Game ===")

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("\nCongratulations! You guessed it right.")
        print("Number:", secret)
        print("Attempts:", attempts)
        break
