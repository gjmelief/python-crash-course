# Exercise 5-7 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Test if favorite fruit is in the favorite fruits list

# The favorite fruits list
favorite_fruits = ['banana', 'apple', 'orange']

# Write If statement the check if a fruit is in the list. Output a message with the tested fruit
# Ask for fruit
fruit = input('Enter a fruit: ').lower()

# The If statements
if fruit in favorite_fruits:
    print(f'You really like {fruit.capitalize()}!')
else:
    print(f'You do not like {fruit.capitalize()}!')