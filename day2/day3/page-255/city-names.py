# 8-6. City Names
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("santiago", "chile"))
print(city_country("lagos", "nigeria"))
print(city_country("nairobi", "kenya"))

# 8-7. Album
def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title,
    }
    if songs:
        album["songs"] = songs
    return album

album_1 = make_album("burna boy", "african giant")
album_2 = make_album("tems", "for broken ears")
album_3 = make_album("wizkid", "made in lagos", 14)

print(album_1)
print(album_2)
print(album_3)

# 8-8. User Albums
while True:
    print("\nEnter album information.")
    print("Enter 'quit' at any time to stop.")

    artist = input("Artist name: ")
    if artist == "quit":
        break

    title = input("Album title: ")
    if title == "quit":
        break

    album = make_album(artist, title)
    print(album)
