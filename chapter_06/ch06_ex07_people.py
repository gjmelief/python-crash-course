# Exercise 6-7 From 'Python Crash Course'
# 08-11-2025 G. Melief

# Exercise for nesting dictionaries in a list and looping through that list

# Three dictionaries
personal_info_01 = {
    'first_name': 'Gert-Jan',
    'last_name': 'Melief',
    'age': 37,
    'city': 'Spijkenisse'
}

personal_info_02 = {
    'first_name': 'Ester',
    'last_name': 'Melief',
    'age': 38,
    'city': 'Spijkenisse'
}

personal_info_03 = {
    'first_name': 'Willem-Alexander',
    'last_name': 'van Oranje',
    'age': 58,
    'city': 'Den Haag'
}

# List with dictionaries
persons = [personal_info_01, personal_info_02, personal_info_03]

# Loop for looping through the list and outputting the personal info
for person in persons:
    print() # for empty line between dictionaries
    for k, v in person.items():
        print(f'{k}: {v}')