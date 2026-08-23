# 6-7. People
person_0 = {
    "first_name": "Ada",
    "last_name": "Lovelace",
    "age": 36,
    "city": "London",
}

person_1 = {
    "first_name": "Bola",
    "last_name": "Ahmed",
    "age": 28,
    "city": "Lagos",
}

person_2 = {
    "first_name": "Chidi",
    "last_name": "Okafor",
    "age": 31,
    "city": "Enugu",
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")

# 6-8. Pets
pet_0 = {"kind": "dog", "owner": "Ada"}
pet_1 = {"kind": "cat", "owner": "Bola"}
pet_2 = {"kind": "parrot", "owner": "Chidi"}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"Kind: {pet['kind']}")
    print(f"Owner: {pet['owner']}\n")

# 6-9. Favorite Places
favorite_places = {
    "ada": ["london", "paris"],
    "bola": ["lagos", "accra", "nairobi"],
    "chidi": ["enugu"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(place.title())

# 6-10. Favorite Numbers
favorite_numbers = {
    "Ada": [8, 16],
    "Bola": [3, 9, 27],
    "Chidi": [21],
    "Dele": [7, 14],
    "Efe": [11, 22],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(number)

# 6-11. Cities
cities = {
    "lagos": {
        "country": "nigeria",
        "population": "15 million",
        "fact": "It is one of the largest cities in Africa.",
    },
    "nairobi": {
        "country": "kenya",
        "population": "5 million",
        "fact": "It is known as the Green City in the Sun.",
    },
    "accra": {
        "country": "ghana",
        "population": "2 million",
        "fact": "It is the capital of Ghana.",
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")

# 6-12. Extensions
cities["lagos"]["food"] = "jollof rice"
cities["nairobi"]["food"] = "nyama choma"
cities["accra"]["food"] = "kelewele"

print("\nUpdated city information:")
for city, info in cities.items():
    print(f"\n{city.title()} is in {info['country'].title()}.")
    print(f"About {info['population']} people live there.")
    print(f"Fact: {info['fact']}")
    print(f"Popular food: {info['food'].title()}")
