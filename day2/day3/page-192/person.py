# 6-1. Person
person = {
    "first_name": "Ada",
    "last_name": "Lovelace",
    "age": 36,
    "city": "London",
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

# 6-2. Favorite Numbers
favorite_numbers = {
    "Ada": 8,
    "Bola": 3,
    "Chidi": 21,
    "Dele": 7,
    "Efe": 11,
}

print(f"Ada's favorite number is {favorite_numbers['Ada']}.")
print(f"Bola's favorite number is {favorite_numbers['Bola']}.")
print(f"Chidi's favorite number is {favorite_numbers['Chidi']}.")
print(f"Dele's favorite number is {favorite_numbers['Dele']}.")
print(f"Efe's favorite number is {favorite_numbers['Efe']}.")

# 6-3. Glossary
glossary = {
    "variable": "A name that stores a value.",
    "string": "A series of characters.",
    "list": "A collection of items in a particular order.",
    "loop": "A way to repeat a block of code.",
    "dictionary": "A collection of key-value pairs.",
}

print(f"variable: {glossary['variable']}\n")
print(f"string: {glossary['string']}\n")
print(f"list: {glossary['list']}\n")
print(f"loop: {glossary['loop']}\n")
print(f"dictionary: {glossary['dictionary']}\n")
