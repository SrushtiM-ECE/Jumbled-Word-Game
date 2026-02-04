import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    if len(password) < 8:
        return "Weak"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if has_upper and has_lower and has_digit and has_special:
        return "Strong"
    else:
        return "Medium"

print("=== Password Generator & Strength Checker ===")

length = int(input("Enter password length: "))
pwd = generate_password(length)

print("Generated Password:", pwd)
print("Password Strength:", check_strength(pwd))
