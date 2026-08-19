# 5-3
alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")

alien_color = "yellow"

if alien_color == "green":
    print("The player just earned 5 points.")

# 5-4
alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")
else:
    print("The player just earned 10 points.")

alien_color = "yellow"

if alien_color == "green":
    print("The player just earned 5 points.")
else:
    print("The player just earned 10 points.")


# 5-5

alien_color = "green"
if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")


alien_color = "yellow"
if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")


alien_color = "red"
if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

# 5-6
age = 15

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# 5-7
favorite_fruits = ["mango", "banana", "apple"]

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "orange" in favorite_fruits:
    print("You really like oranges!")

if "grape" in favorite_fruits:
    print("You really like grapes!")