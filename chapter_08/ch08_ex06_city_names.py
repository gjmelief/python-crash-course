# Exercise 8-6 From 'Python Crash Course'
# 25-11-2025 G. Melief

# Exercise defining a function and return a value

def city_country(city, country):
    '''Display the city and country neatly formatted'''
    # city_country_string = f'{city}, {country}'
    # return city_country_string.title()
    return f'{city}, {country}'.title() # Direct return for simplicity

city_country_output = city_country('spijkenisse', 'the netherlands')
print(city_country_output)

city_country_output = city_country('london', 'england')
print(city_country_output)

city_country_output = city_country('paris', 'france')
print(city_country_output)