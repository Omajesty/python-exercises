from random import choice


lottery_items = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
)

winning_numbers = []

while len(winning_numbers) < 4:
    item = choice(lottery_items)

    if item not in winning_numbers:
        winning_numbers.append(item)


print("The winning ticket is:")

for item in winning_numbers:
    print(item)

print("\nAny ticket matching these 4 numbers or letters wins a prize!")