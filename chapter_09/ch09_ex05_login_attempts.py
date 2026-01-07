# Exercise 9-4 From 'Python Crash Course'
# 07-01-2026 G. Melief

# Exercise modifying the values inside an instance

class User:
    '''A class describing information about a user'''


    def __init__(self, first_name, last_name, age, location):
        '''Initialize attributes to describe a user'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        '''Method for printing information about a user'''
        print(f"\nThe user's name is {self.first_name.capitalize()} "
            f"{self.last_name.capitalize()}. The user is {self.age} years old "
            f"and lives in {self.location.title()}")

    def greet_user(self):
        '''Method for printing a personalized greeting to the user'''
        print(f"\nHello {self.first_name.capitalize()} {self.last_name.capitalize()}. "
              f"How is the weather in {self.location.title()}?")

    def increment_login_attempts(self):
        '''Method for incrementing the login attempts with +1'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Method for resetting the login attempt to 0'''
        self.login_attempts = 0

# Create instance of the User class
user0 = User('Gert-Jan', 'Melief', 37, 'Spijkenisse')

# Testing the increment and reset method's
print(f"{user0.first_name.capitalize()} has {user0.login_attempts} login attempts")
user0.increment_login_attempts()
user0.increment_login_attempts()
user0.increment_login_attempts()
print(f"{user0.first_name.capitalize()} has {user0.login_attempts} login attempts")
user0.reset_login_attempts()
print(f"{user0.first_name.capitalize()} has {user0.login_attempts} login attempts")