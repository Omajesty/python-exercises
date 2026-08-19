# 4-10. Slices
pizzas = ["chicken pizza", "beef pizza", "peperoni pizza", "veggie pizza", "Margherita"]

print("The first three items in the list are:")

for pizza in pizzas[:3]:
    print(pizza.title())

print("Three items from the middle of the list are:")

for pizza in pizzas[1:4]:
    print(pizza.title())

print("The last three items in the list are:")

for pizza in pizzas[-3:]:
    print(pizza.title())

# 4-11. My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append("hawaiian pizza")
friend_pizzas.append("cheese pizza")
print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza.title())

print("My friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza.title())

# 4-12. More Loops
my_foods = ["pizza", "falafel", "carrot cake"]

friend_foods = my_foods[:]

print("My favorite foods are:")

for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")

for food in friend_foods:
    print(food)