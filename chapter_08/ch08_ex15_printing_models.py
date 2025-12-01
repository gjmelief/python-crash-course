# Exercise 8-15 From 'Python Crash Course'
# 01-12-2025 G. Melief

# Exercise using import

# Module locating the program functions
import ch08_ex15_printing_functions as pf

# Program simulates printing designs, until none are left.
# Designs move to results after printing.
# Use print_models('design1', 'design2', etc)
# The printed models will be stored in result
result = pf.print_models('design1', 'design2')
# Displaying the completed models
pf.show_completed_models(result)