from pathlib import Path

# 10-6. Addition
print("Give me two numbers and I will add them.")
first_number = input("First number: ")
second_number = input("Second number: ")

try:
    result = int(first_number) + int(second_number)
except ValueError:
    print("Please enter a number, not text.")
else:
    print(f"The sum is {result}.")

# 10-7. Addition Calculator
print("\nGive me two numbers and I will add them.")
print("Enter 'quit' to stop.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "quit":
        break

    second_number = input("Second number: ")
    if second_number == "quit":
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter a number, not text.")
    else:
        print(f"The sum is {result}.")

# 10-8. Cats and Dogs
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} was not found.")
    else:
        print(contents)

# 10-9. Silent Cats and Dogs
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contents)

# 10-10. Common Words
filenames = ["sample_text.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} was not found.")
    else:
        the_count = contents.lower().count("the")
        the_space_count = contents.lower().count("the ")
        print(f"The word 'the' appears about {the_count} times in {path}.")
        print(f"The phrase 'the ' appears about {the_space_count} times in {path}.")
