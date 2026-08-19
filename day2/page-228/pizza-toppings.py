# 7-4
prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished. "

topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")

# 7-5
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished. "

age = ""
while age != "quit":
    age = input(prompt)
    if age != "quit":
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
        age = ""

# 7-6
# Use a conditional
prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished. "

topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")

# Use an active variable
prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished. "

active = True
while active:
    topping = input(prompt)
    if topping == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

# Use break 
prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"I'll add {topping} to your pizza.")

# 7-7

while True:
     print("This loop never ends!")
