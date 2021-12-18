class User():
    def __init__(self,first_name,last_name,username,email,number,age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.number = number
        self.age = age
        self.login_attemps = 0
    
    def describe_user(self):
        print("  NAME:  ", self.first_name)
        print("  LAST NAME:  ", self.last_name)
        print("  USERNAME:  ", self.username)
        print("  EMAIL:  ", self.email)
        print("  NUMBER:  ", self.number)
        print("  AGE:  ", self.age)
    
    def greet_user(self):
        print("Welcome ", self.username)
    
    def increment_login_attemps(self):
        self.login_attemps += 1
    
    def reset_login_attemps(self):
        self.login_attemps = 0
        
    

user1 = User("Anahi", "De la Cruz", "Elvanana", "elva960@hotmail.com", "8441234567", "16")
user1.greet_user()
user1.describe_user()
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
print("  Intentos de inicio de sesion: ", user1.login_attemps)
user1.reset_login_attemps()
print("  Intentos de inicio de sesion: ", user1.login_attemps)
user1.increment_login_attemps()
user1.increment_login_attemps()
print("  Intentos de inicio de sesion: ", user1.login_attemps)

