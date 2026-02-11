import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("---- Password Generator ----")

length = int(input("Enter the desired password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    password = generate_password(length)
    print("Generated Password:", password)
