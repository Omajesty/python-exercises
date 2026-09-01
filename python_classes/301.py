# 9-6. Ice Cream Stand
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    
    def describe_restuarant(self):
        print(f"{self.restaurant_name} have different yummy {self.cuisine_type}s")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now Open")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Pineapple", "Vanilla", "Strawberry"]
        
    def display_flavors(self):
        print("Available ice cream flavors:")
        
        for flavor in self.flavors:
            print(f"- {flavor}")

jovit_icecream = IceCreamStand("Jovit Icecream", "Ice Cream")

jovit_icecream.describe_restuarant()
jovit_icecream.display_flavors()

# 9-7. Admin
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

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, occupation):
        super().__init__(first_name, last_name, gender, age, occupation)
        
        self.privileges = ["can add post", "cand delete post", "can ban user"]
        
    def show_privileges(self):
        print("Admin privileges:")
        
        for privilege in self.privileges:
            print(f"-{privilege}")

admin_user = Admin("Majesty", "Onuzurike", "Male", "19", "Software Engineer")

admin_user.show_privileges()

# 9-8. Privileges
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

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, occupation):
        super().__init__(first_name, last_name, gender, age, occupation)
        
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "cand delete post", "can ban user"]        
    def show_privileges(self):
        print("Admin privileges:")
        
        for privilege in self.privileges:
            print(f"-{privilege}")

new_admin = Admin("Munachi", "Obosi", "Female", 24, "Nurse")
new_admin.privileges.show_privileges()

# 9-9. Battery Upgrade:
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted decriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=40):
        """Initializes the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it isn't already 65 kWh."""

        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()

my_leaf.battery.get_range()