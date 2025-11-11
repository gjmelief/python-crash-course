# Exercise 6-8 From 'Python Crash Course'
# 11-11-2025 G. Melief

# Exercise for looping through nested dictionaries in a list

# Dictionaries with information about pets
rex = {'name': 'rex',
       'species': 'cat',
       'owner': 'ester',
       }

storm = {'name': 'storm',
         'species': 'dog',
         'owner': 'mirjam'}

pets = [rex, storm] # List of the dictionaries

# for loop for printing the information
for pet in pets:
    print() # Print statement for empty line between pets
    for k, v in pet.items():
        print(f'The {k} is: {v}')

# All the information in one line
for pet in pets:
    print(f'\nThe name of the pet is {pet['name'].title()}, '
           f'the species is {pet['species']}, '
           f'and the owner is {pet['owner'].title()}')