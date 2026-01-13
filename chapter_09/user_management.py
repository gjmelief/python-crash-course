"""A set of classes representing user roles and their privileges"""

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

class Privileges:
    '''
    Create subclass from the Admin Class
    Store the privileges in this subclass
    '''


    def __init__(self):
        '''Define the attributes of the Class'''
        self.privileges = ['can add post',
                           'can delete post',
                           'can modify post',
                           'can (un)ban user']

    def show_privileges(self):
        '''Method for displaying the privileges of the admin account'''
        print(f"The admin role has the following privileges: ")
        for privilege in self.privileges:
            print(f"\t{privilege.capitalize()}")

class Admin(User):
    '''
    Create a subclass from the User Class
    Admin class for describing privileges for the Admin User account
    '''


    def __init__(self, first_name, last_name, age, location):
        '''Initialize the attributes for the Admin Class'''
        super().__init__(first_name, last_name, age, location)
        # A Privilege class instance as an attribute in the Admin class
        self.privileges = Privileges()