# Exercise 6-5 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Exercise for using loops with dictionaries

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# list of people wou should take a poll
names = ['jen', 'sarah', 'gert-jan', 'ester', 'boris', 'valerie']


for name in names: # Loop through the names list
    if name in favorite_languages.keys(): # Test for name in the dict
        print(f'{name}, Thank you for taking the poll')
    else:
        print(f'{name}, please take the test')