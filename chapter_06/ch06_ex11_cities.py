# Exercise 6-11 From 'Python Crash Course'
# 12-11-2025 G. Melief

# Exercise for displaying a dictionary in a dictionary

cities = {
    'rotterdam': {
        'country': 'netherlands',
        'population': 750000,
        'fact': 'biggest port of europe',
    },
    'tokyo': {
        'country': 'japan',
        'population': 37400000,
        'fact': 'largest metropolitan area in the world',
    },
    'mumbai': {
        'country': 'india',
        'population': 20900000,
        'fact': 'home to bollywood film industry',
    },
}

# Print the name of the city with all the information
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = city_info["country"]
    population = city_info["population"]
    fact = city_info["fact"]
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact.capitalize()}")