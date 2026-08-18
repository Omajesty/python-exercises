# Exercise 24
post = "Loving #Python and #Coding at #LkhibraAcademy"
words_in_post = post.split()
hashtags = []

for word in words_in_post:
    if word.startswith("#"):
        hashtags.append(word)

print(f"Hashtags: {hashtags}")