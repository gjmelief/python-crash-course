# Exercise 11-2 From 'Python Crash Course'
# 27-01-2026 G. Melief

# Exercise using pytest

# Exercise 11-1 From 'Python Crash Course'
# 27-01-2026 G. Melief

# Exercise using pytest

def formatted_city_country(city, country, population=''):
    """A function that returns a formatted 'City', "Country"""
    if population:
        city_country = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country