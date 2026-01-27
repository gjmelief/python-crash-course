# Exercise 11-1 From 'Python Crash Course'
# 27-01-2026 G. Melief

# Exercise using pytest

def formatted_city_country(city, country):
    """A function that returns a formatted 'City', "Country"""
    city_country = f"{city}, {country}"
    return city_country.title()