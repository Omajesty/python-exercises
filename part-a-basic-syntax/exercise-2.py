# Exercise 2
stud_morn = 15
stud_eve = 25

print(f"Before Swap: Morning Batch = {stud_morn}, Evening Batch = {stud_eve}")

stud_morn, stud_eve = stud_eve, stud_morn

print(f"After Swap: Morning Batch = {stud_morn}, Evening Batch = {stud_eve}")
