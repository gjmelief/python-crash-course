# Exercise 5-10 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Exercise for looping through a list and outputting a msg

# A list with numbers 1 to 9
numbers = list(range(1, 10))

# Loop through the list and output the ordinal numbers
for number in numbers:
    if number == 1:
        ordinal = 'st'
    elif number == 2:
        ordinal = 'nd'
    elif number == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    print(f'{number}{ordinal}')