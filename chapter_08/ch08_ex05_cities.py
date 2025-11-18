# Exercise 8-5 From 'Python Crash Course'
# 18-11-2025 G. Melief

# Exercise defining a function with default parameters and calling the function
# with different methods

def describe_city(city_name, country= "the netherlands"):
    """Display information about the country"""
    print(f"{city_name.title()} is in {country.title()}.")

# Display the message with the default parameter
describe_city("den haag")

# Display the message with different arguments
describe_city("spijkenisse")

# Display the message with different arguments
describe_city("london", "england")