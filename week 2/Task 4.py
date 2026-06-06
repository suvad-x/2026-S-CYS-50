import random
length = int(input("Eter length of password: "))
upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
digits = input("Include digits? (yes/no): ").lower() == "yes"
special = input("Include special characters? (yes/no): ").lower() == "yes"
chars = ""
if upper:
    chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lower:
    chars += "abcdefghijklmnopqrstuvwxyz"
if digits:
    chars += "0123456789"
if special:
    chars += "!@#$%^&*()_+-=[]{}|;:,.<>/?"
if chars == "":
    print("You must select at least one character type!")
else:
    password = ""
    for i in range(length):
        password += random.choice(chars)
    print("Your password is:", password)