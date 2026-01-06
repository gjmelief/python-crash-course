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
    print(f"The user's name is {self.first_name.capitalize()}"
          f"{self.last_name.capitalize()}. The user is {self.age} year's old"
          f"and lives in {self.location.capitalize()}")
