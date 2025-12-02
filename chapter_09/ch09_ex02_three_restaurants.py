# Exercise 9-2 From 'Python Crash Course'
# 02-12-2025 G. Melief

# Exercise using three instances from a class

class Restaurant:
    '''A class describing information about a restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize attributes to describe a restaurant'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Display the attributes of the restaurant'''
        print(f"\nThe name of the restaurant is {self.restaurant_name.capitalize()}."
                f"\nThey are serving {self.cuisine_type} food.")

    def open_restaurant(self):
        '''Display a message stating the restaurant is open'''
        print(f"\n{self.restaurant_name.capitalize()} is open")


# Make three instances of the Restaurant class
restaurant0 = Restaurant("fallow", "english")
restaurant1 = Restaurant("noma", "danish")
restaurant2 = Restaurant("librije", "dutch")

# Call the method describe_restaurant with the instances
restaurant0.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()