# Exercise 9-3 From 'Python Crash Course'
# 06-01-2026 G. Melief

# Exercise creating a Class and creating several instances

class User:
    '''A class describing information about a user'''


    def __init__(self, first_name, last_name, age, location):
        '''Initialize attributes to describe a user'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        '''Method for printing information about a user'''
        print(f"\nThe user's name is {self.first_name.capitalize()} "
            f"{self.last_name.capitalize()}. The user is {self.age} years old "
            f"and lives in {self.location.title()}")

    def greet_user(self):
        '''Method for printing a personalized greeting to the user'''
        print(f"\nHello {self.first_name.capitalize()} {self.last_name.capitalize()}. "
              f"How is the weather in {self.location.title()}?")

# Create several instances representing different users
user0 = User('gert-jan', 'melief', 37, 'the netherlands')
user1 = User('henk', 'smit', 42, 'germany')
user2 = User('john', 'doe', 54, 'the united kingdom')

# Call both method from the Users class for different users
user0.describe_user()
user0.greet_user()
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()