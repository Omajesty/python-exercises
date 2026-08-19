# 5-1
car = "subaru"
age = 18

print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

print("\nIs car != 'audi'? I predict True.")
print(car != "audi")

print("\nIs car != 'subaru'? I predict False.")
print(car != "subaru")

print("\nIs age == 18? I predict True.")
print(age == 18)

print("\nIs age == 20? I predict False.")
print(age == 20)

print("\nIs age > 15? I predict True.")
print(age > 15)

print("\nIs age < 15? I predict False.")
print(age < 15)

print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs age <= 15? I predict False.")
print(age <= 15)

# 5-2
# 1. Equality and inequality with strings

name = "Samuel"

print("Is name == 'Samuel'? I predict True.")
print(name == "Samuel")

print("\nIs name != 'Peter'? I predict True.")
print(name != "Peter")

print("\nIs name == 'Peter'? I predict False.")
print(name == "Peter")


# 2. Tests using lower()

print("\nIs name.lower() == 'samuel'? I predict True.")
print(name.lower() == "samuel")

print("\nIs name.lower() == 'peter'? I predict False.")
print(name.lower() == "peter")


# 3. Numerical tests

age = 18

print("\nIs age == 18? I predict True.")
print(age == 18)

print("\nIs age != 18? I predict False.")
print(age != 18)

print("\nIs age > 15? I predict True.")
print(age > 15)

print("\nIs age < 15? I predict False.")
print(age < 15)

print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs age <= 15? I predict False.")
print(age <= 15)


# 4. Tests using and

print("\nIs age >= 18 and age < 25? I predict True.")
print(age >= 18 and age < 25)

print("\nIs age >= 18 and age > 25? I predict False.")
print(age >= 18 and age > 25)


# 5. Tests using or

print("\nIs age == 18 or age == 20? I predict True.")
print(age == 18 or age == 20)

print("\nIs age == 15 or age == 20? I predict False.")
print(age == 15 or age == 20)


# 6. Tests using in

foods = ["rice", "beans", "yam", "chicken"]

print("\nIs 'rice' in foods? I predict True.")
print("rice" in foods)

print("\nIs 'pizza' in foods? I predict False.")
print("pizza" in foods)


# 7. Tests using not in

print("\nIs 'pizza' not in foods? I predict True.")
print("pizza" not in foods)

print("\nIs 'rice' not in foods? I predict False.")
print("rice" not in foods)