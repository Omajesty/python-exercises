# Exercise 30
original_text = input("Enter a word or phrase: ")
cleaned_text = original_text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print(f"{original_text} is a palindrome!")
else:
    print(f"{original_text} is not a palindrome.")
