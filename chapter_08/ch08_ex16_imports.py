# Exercise 8-15 From 'Python Crash Course'
# 01-12-2025 G. Melief

# Exercise using multiple styles of import

import ch08_ex15_printing_functions
from ch08_ex15_printing_functions import print_models
from ch08_ex15_printing_functions import print_models as pm
import ch08_ex15_printing_functions as pf
from ch08_ex15_printing_functions import *

ch08_ex15_printing_functions.print_models('design1', 'design2')
print_models('design1', 'design2')
pm('design1', 'design2')
pf.print_models('design1', 'design2')
result = print_models('design1', 'design2')
show_completed_models(result)
