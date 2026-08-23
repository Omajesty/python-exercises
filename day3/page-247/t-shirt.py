# 8-3. T-Shirt
def make_shirt(size, message):
    print(f"The shirt size is {size} and the message is '{message}'.")

make_shirt("medium", "Hello World")
make_shirt(size="large", message="Python is fun")

# 8-4. Large Shirts
def make_shirt(size="large", message="I love Python"):
    print(f"The shirt size is {size} and the message is '{message}'.")

make_shirt()
make_shirt("medium")
make_shirt("small", "Code every day")

# 8-5. Cities
def describe_city(city, country="nigeria"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("lagos")
describe_city("abuja")
describe_city("accra", "ghana")
