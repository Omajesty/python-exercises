# Exercise 17

first, second, third = input("Enter three numbers: ").split()
first = int(first)
second = int(second)
third = int(third)

if first >= second and first >= third:
    largest = first
elif second >= first and second >= third:
    largest = second
else:
    largest = third

print(f"The largest number is {largest}.")
