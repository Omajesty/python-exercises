# 7-8
sandwich_orders = ["tuna", "turkey", "ham", "chicken"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-9
sandwich_orders = ["tuna", "pastrami", "turkey", "pastrami", "ham", "pastrami", "chicken"]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-10
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")
