"""A class used to represent a restaurant."""

class Restaurant:
    '''A class describing information about a restaurant'''


    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize attributes to describe a restaurant'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Display the attributes of the restaurant'''
        print(f"\nThe name of the restaurant is {self.restaurant_name.capitalize()}."
                f"\nThey are serving {self.cuisine_type} food.")

    def open_restaurant(self):
        '''Display a message stating the restaurant is open'''
        print(f"\n{self.restaurant_name.capitalize()} is open")

    def set_number_served(self, served):
        '''Method for updating the number_served value'''
        if served >= self.number_served:
            self.number_served = served
            print(f"Customers served: {self.number_served}")
        else:
            print("You can't 'unserve' customers!")

    def increment_number_served(self, served):
        '''Method for updating the number_served value with increment'''
        self.number_served += served