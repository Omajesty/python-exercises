# 6-4. Glossary 2
glossary = {
    "variable": "A name that stores a value.",
    "string": "A series of characters.",
    "list": "A collection of items in a particular order.",
    "loop": "A way to repeat a block of code.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A named block of code that does one job.",
    "boolean": "A value that is either True or False.",
    "tuple": "A list of items that cannot be changed.",
    "if statement": "A way to run code only when a condition is true.",
    "comment": "A note in your program that Python ignores.",
}

for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")

# 6-5. Rivers
rivers = {
    "nile": "egypt",
    "niger": "nigeria",
    "amazon": "brazil",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe rivers in this dictionary are:")
for river in rivers.keys():
    print(river.title())

print("\nThe countries in this dictionary are:")
for country in rivers.values():
    print(country.title())

# 6-6. Polling
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

people = ["jen", "sarah", "edward", "phil", "mike", "linda"]

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take our favorite languages poll.")
