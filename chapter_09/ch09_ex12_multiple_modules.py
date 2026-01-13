# Exercise 9-12 From 'Python Crash Course'
# 13-01-2026 G. Melief

# Exercise for practicing importing modules

from user_management import Admin

admin_gj = Admin('Gert-Jan', 'Melief', 37, 'Spijkenisse')
admin_gj.privileges.show_privileges()