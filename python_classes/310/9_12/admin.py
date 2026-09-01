from user import User

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "cand delete post", "can ban user"]        
    def show_privileges(self):
        print("Admin privileges:")
        
        for privilege in self.privileges:
            print(f"-{privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, occupation):
        super().__init__(first_name, last_name, gender, age, occupation)
        
        self.privileges = Privileges()
