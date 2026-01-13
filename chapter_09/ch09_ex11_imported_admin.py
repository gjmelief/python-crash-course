# Exercise 9-11 From 'Python Crash Course'
# 13-01-2026 G. Melief

# Exercise for practicing importing modules

import user_management as um

admin_gj = um.Admin('Gert-Jan', 'Melief', 37, 'Spijkenisse')
admin_gj.privileges.show_privileges()