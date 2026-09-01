from random import choice


lottery_items = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
)

my_ticket = [7, "C", 2, "E"]

attempts = 0

while True:
    winning_numbers = []

    while len(winning_numbers) < 4:
        item = choice(lottery_items)

        if item not in winning_numbers:
            winning_numbers.append(item)

    attempts += 1

    if winning_numbers == my_ticket:
        break

print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winning_numbers}")
print(f"It took {attempts} attempts to win.")