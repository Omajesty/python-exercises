# 8-12. Sandwiches
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("cheese")
make_sandwich("turkey", "lettuce")
make_sandwich("chicken", "tomato", "mayo")

# 8-13. User Profile
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

my_profile = build_profile(
    "samuel",
    "onuzu",
    location="lagos",
    field="programming",
    hobby="football",
)
print(my_profile)

# 8-14. Cars
def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
