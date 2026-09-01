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
