# Exercise 25
password = input("Enter a password: ")

has_number = False
has_special = False
special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

for character in password:
    if character.isdigit():
        has_number = True
    if character in special_characters:
        has_special = True

if len(password) >= 8 and has_number and has_special:
    print("This password is strong.")
else:
    print("This password is weak.")
    print("It must have at least 8 characters, a number, and a special character.")
