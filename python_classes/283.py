# 9-1. Restaurant:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    
    def describe_restuarant(self):
        print(f"The name of this restaurant is, {self.restaurant_name}. They have {self.cuisine_type} cuisine")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now Open")
        
# 9-2. Three Restaurants:
ntachi_ossa = Restaurant("Ntachi Ossa", "Ofada rice")
ntachi_ossa.describe_restuarant()

decastle_resort = Restaurant("De Castle Resort", "Fried rice")
decastle_resort.describe_restuarant()

roots = Restaurant("Roots Restaurant", "Amala and Ewedu")
roots.describe_restuarant()

decastle_resort.open_restaurant()

# 9-3. Users:
class User:
    def __init__(self, first_name, last_name, gender, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.occupation = occupation
        
    def describe_user(self):
        print(f"-----------BIO DATA-----------")
        print(f"Fullname:\t {self.first_name} {self.last_name}")
        print(f"Gender: \t {self.gender}")
        print(f"Age: \t \t {self.age}")
        print(f"Occupation: \t {self.occupation}")
        print(f"------------------------------")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}. Welcome!")
        
stella = User("Stella", "Ndubuisi", "Female", 30, "Teacher")
stella.describe_user()
stella.greet_user()

muna = User("Munachi", "Obosi", "Female", 24, "Nurse")
muna.describe_user()
muna.greet_user()
