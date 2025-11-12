# Exercise 6-10 From 'Python Crash Course'
# 12-11-2025 G. Melief

# Exercise for looping through a dictionary with keys and a list as value

fav_num = {
    'Hennie' : [13, 23],
    'Gert-Jan' : [42, 52],
    'Ester' : [25, 35],
    'Astrid' : [26, 36],
    'Boris' : [22, 32],
    'Valerie' : [28, 38],
}

# Print all the information from the dictionary
for name, numbers in fav_num.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
            print(f'\t{number}')