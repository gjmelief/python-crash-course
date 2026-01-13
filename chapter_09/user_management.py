"""A set of classes representing user roles and their privileges"""

from user import User
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