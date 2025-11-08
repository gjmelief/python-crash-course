# Exercise 6-3 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Exercise to make a glossary and output neatly the key:value pairs

# The glossary
glossary = {
    'variable': 'a name that refers to a value in memory',
    'function': 'a reusable block of code that performs a specific task',
    'loop': 'a structure that executes code repeatedly',
    'dictionary': 'a collection of key-value pairs for structured data',
    'parameter': 'a variable in a function definition that receives input'
}

# Use print function to output the glossary in a neat way
print(f'variable:\n{glossary["variable"].capitalize()}')
print(f'\nfunction:\n{glossary["function"].capitalize()}')
print(f'\nloop:\n{glossary["loop"].capitalize()}')
print(f'\ndictionary:\n{glossary["dictionary"].capitalize()}')
print(f'\nparameter:\n{glossary["parameter"].capitalize()}')