# 9-4. Number Served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    
    def describe_restuarant(self):
        print(f"The name of this restaurant is, {self.restaurant_name}. They have {self.cuisine_type} cuisine")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now Open")
        
    def set_number_served(self, served_customers):
        self.number_served = served_customers
    
    def increment_number_served(self, add_served_customers):
        self.number_served += add_served_customers
        
        
    def show_served_customers(self):
        print(f"The number of customers serverd in {restuarant.restaurant_name} is {restuarant.number_served}")

restuarant = Restaurant("Nkechi's Buka", "Coconut Rice")
restuarant.show_served_customers()


restuarant.number_served = 10
restuarant.show_served_customers()

restuarant.set_number_served(25)
restuarant.show_served_customers()

restuarant.increment_number_served(8)
restuarant.show_served_customers()

# 9-5. Login Attempts: 
class User:
    def __init__(self, first_name, last_name, gender, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0
        
    def increment_login_attempts(self):
        self.login_attempts +=1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

stella = User("Stella", "Ndubuisi", "Female", 30, "Teacher")
stella.increment_login_attempts()
stella.increment_login_attempts()
stella.increment_login_attempts()

print(f"Login attempts: {stella.login_attempts}")

stella.reset_login_attempts()
print(f"Login attempts after reset: {stella.login_attempts}")
