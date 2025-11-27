# Exercise 8-12 From 'Python Crash Course'
# 27-11-2025 G. Melief

# Exercise using *args and a function

def build_sandwich(*toppings):
    '''Build a function printing the toppings for a sandwich'''
    print('\nYou ordered a sandwich with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

build_sandwich('ham')
build_sandwich('tomato', 'cheese')
build_sandwich('tuna', 'cheese', 'mayonnaise')