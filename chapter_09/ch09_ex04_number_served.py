# Exercise 9-4 From 'Python Crash Course'
# 06-01-2026 G. Melief

# Exercise creating a Class and modifying the attributes of the instances

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

# Create instance of the Restaurant Class
restaurant = Restaurant('fallow', 'english')

# Print the number of customers served
print(f"Customers served: {restaurant.number_served}")