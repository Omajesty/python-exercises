# Counting to Twenty
for num in range(1,21):
    if num <21:
        print(num)

# One Million
numbers = list(range(1,1000001))
# for num in numbers:
#     print(num)

# min and max and summing a million
print (min(numbers))
print (max(numbers))
print (sum(numbers))

# Odd Numbers
odd_numbers = list(range(1, 21, 2))
for odd_num in odd_numbers:
    print(odd_num)

# Multiples of three
multiples_three = list(range(3, 31, 3))
for threes in multiples_three:
    print(threes)

# Cubes from 1 to 10
cubes_in_10 = list(range(1, 11))
for cube_num in cubes_in_10:
    print(f"{cube_num**3}")

# Cube Comprehension
comp_cubes = [i**3 for i in range(1, 11)]
print(comp_cubes)