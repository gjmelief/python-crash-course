# Exercise 6-2 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Exercise for storing information in a dictionary and printing the info

# Make a dictionary with person : fav number pairs
fav_num = {
    'Hennie' : '13',
    'Gert-Jan' : '42',
    'Ester' : '25',
    'Astrid' : '26',
    'Boris' : '22',
    'Valerie' : '28',
}

# Output the names and numbers
print(f'Astrid: {fav_num['Astrid']}')
print(f'Boris: {fav_num["Boris"]}')
print(f'Ester: {fav_num["Ester"]}')
print(f'Gert-Jan: {fav_num["Gert-Jan"]}')
print(f'Hennie: {fav_num["Hennie"]}')
print(f'Valerie: {fav_num["Valerie"]}')