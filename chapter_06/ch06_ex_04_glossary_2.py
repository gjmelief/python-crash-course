# Exercise 6-4 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Exercise to make a glossary and output neatly the key:value pairs

# The glossary
glossary = {
    'variable': 'a name that refers to a value in memory',
    'function': 'a reusable block of code that performs a specific task',
    'loop': 'a structure that executes code repeatedly',
    'dictionary': 'a collection of key-value pairs for structured data',
    'parameter': 'a variable in a function definition that receives input',
    'argument': 'the actual value passed to a function when calling it',
    'list': 'an ordered collection of items that can be modified',
    'string': 'a sequence of characters used to represent text',
    'boolean': 'a data type with only two possible values: True or False',
    'index': 'a number that represents the position of an item in a sequence'
}

# Use a for loop the output the dictionary neatly. Sorted() for sorting
for word, meaning in sorted(glossary.items()):
    print(f'\n{word.title()}:\n{meaning.capitalize()}')