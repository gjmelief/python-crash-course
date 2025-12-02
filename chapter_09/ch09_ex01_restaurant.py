# Exercise 9-1 From 'Python Crash Course'
# 02-12-2025 G. Melief

# Exercise introducing classes

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


# Make an instance of the Restaurant class
restaurant_info = Restaurant("fallow", "english")

# Print the two attributes
print(f"The name of the restaurant is {restaurant_info.restaurant_name.capitalize()}.")
print(f"They are serving {restaurant_info.cuisine_type} food.")

# Call the methods defined in the Restaurant class
restaurant_info.describe_restaurant()
restaurant_info.open_restaurant()