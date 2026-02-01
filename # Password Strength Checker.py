# Password Strength Checker

import string

def check_password(password):
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

pwd = input("Enter your password: ")
result = check_password(pwd)

print("Password Strength:", result)
