# Exercise 8-15 From 'Python Crash Course'
# 01-12-2025 G. Melief

# Exercise using import

import ch08_ex15_printing_functions as pf

'''
Simulate printing each design, until none are left.
Move each design to completed_models after printing.
Use print_models(unprinted_designs, completed_models)
'''
unprinted_designs = ["test1", "test2"]
completed_models = []
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)