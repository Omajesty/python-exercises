# Python Exercises

A collection of Python exercises completed while learning and practicing core Python programming concepts.

The exercises cover topics including lists, slicing, tuples, loops, conditional tests, `if` statements, and basic algorithmic problem solving.

## Exercises Covered

### Chapter 4 - Lists

#### Exercise 4-10: Slices

Practiced using list slices to access:

* The first three items in a list
* Three items from the middle of a list
* The last three items in a list

Example:

```python
pizzas[:3]
pizzas[1:4]
pizzas[-3:]
```

#### Exercise 4-11: My Pizzas, Your Pizzas

Practiced:

* Copying lists using slicing
* Creating independent lists
* Adding items with `.append()`
* Iterating through lists with `for` loops

Example:

```python
friend_pizzas = pizzas[:]

pizzas.append("hawaiian pizza")
friend_pizzas.append("cheese pizza")
```

The exercise demonstrates that `pizzas` and `friend_pizzas` are separate lists.

#### Exercise 4-12: More Loops

Practiced using `for` loops to print every item in multiple lists.

Example:

```python
for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)
```

#### Exercise 4-13: Buffet

Introduced tuples and practiced:

* Creating tuples
* Iterating through tuples
* Understanding tuple immutability
* Attempting to modify a tuple
* Reassigning a tuple with a revised menu

Example:

```python
foods = ("rice", "beans", "chicken", "yam", "salad")
```

A tuple does not allow individual items to be changed:

```python
foods[0] = "pasta"
```

This produces a `TypeError`.

A new tuple can instead be assigned:

```python
foods = ("pasta", "fish", "chicken", "yam", "salad")
```

---

# Chapter 5 - If Statements

### Exercise 5-1: Conditional Tests

Practiced Boolean conditional tests using:

* Equality `==`
* Inequality `!=`
* Greater than `>`
* Less than `<`
* Greater than or equal to `>=`
* Less than or equal to `<=`

The exercise included at least ten tests, with five evaluating to `True` and five evaluating to `False`.

Example:

```python
car = "subaru"

print(car == "subaru")
print(car == "audi")
```

### Exercise 5-2: More Conditional Tests

Expanded conditional testing to include:

* String equality and inequality
* The `lower()` method
* Numerical comparisons
* `and`
* `or`
* `in`
* `not in`

Example:

```python
name.lower() == "samuel"

age >= 18 and age < 25

"rice" in foods

"pizza" not in foods
```

---

### Exercise 5-3: Alien Colors #1

Practiced a basic `if` statement.

If the alien is green, the player earns 5 points.

```python
alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")
```

Also tested a version where the condition is false and produces no output.

---

### Exercise 5-4: Alien Colors #2

Introduced the `if-else` structure.

```text
Green alien
    ↓
5 points

Any other color
    ↓
10 points
```

Example:

```python
if alien_color == "green":
    print("The player just earned 5 points.")
else:
    print("The player just earned 10 points.")
```

---

### Exercise 5-5: Alien Colors #3

Practiced an `if-elif-else` chain with three possible outcomes:

```text
Green  → 5 points
Yellow → 10 points
Red    → 15 points
```

Example:

```python
if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")
```

---

### Exercise 5-6: Stages of Life

Practiced using an `if-elif-else` chain to classify a person's age.

| Age     | Stage    |
| ------- | -------- |
| Under 2 | Baby     |
| 2–3     | Toddler  |
| 4–12    | Kid      |
| 13–19   | Teenager |
| 20–64   | Adult    |
| 65+     | Elder    |

Example:

```python
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
```

---

### Exercise 5-7: Favorite Fruit

Practiced using multiple **independent `if` statements** and the `in` operator.

```python
favorite_fruits = ["mango", "banana", "apple"]

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "apple" in favorite_fruits:
    print("You really like apples!")
```

Unlike an `if-elif-else` chain, each `if` statement is evaluated independently.

---

# Algorithm Practice

## Two Sum

Implemented a solution to the classic Two Sum problem.

Given a list of integers and a target value, the program finds the indices of two numbers whose sum equals the target.

Example:

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

### Solution

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

### Concepts Practiced

* Functions
* Parameters
* Lists
* Indexing
* `for` loops
* Nested loops
* Conditional statements
* `return`
* Algorithmic thinking

### Complexity

The current solution uses nested loops.

* **Time complexity:** `O(n²)`
* **Space complexity:** `O(1)`

---

# Key Python Concepts Practiced

Through these exercises, the following concepts have been practiced:

* Variables
* Strings
* Integers
* Lists
* List indexing
* List slicing
* List copying
* `.append()`
* Tuples
* Tuple immutability
* `for` loops
* Nested loops
* Conditional tests
* Boolean values
* `if`
* `elif`
* `else`
* Comparison operators
* Logical operators
* Membership operators
* String `.lower()`
* Functions
* Parameters
* `return`
* Basic algorithmic problem solving

## Goal

The goal of these exercises is not simply to produce working code, but to develop a strong understanding of Python fundamentals and the ability to reason through programming problems without relying entirely on pre-written solutions.
