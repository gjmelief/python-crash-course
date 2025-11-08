# Exercise 6-5 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Exercise practicing dictionaries and loops

# The dictionary rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'rhine': 'germany'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f'The river {river.title()} runs through the country {country.title()}')

# Empty line
print()

# Loop through the dictionary and output the rivers
for river in rivers:
    print(river)

# Empty Line
print()
# Loop through the dictionary and output the country's
for country in rivers.values():
    print(country)