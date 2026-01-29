# Exercise 11-3 From 'Python Crash Course'
# 27-01-2026 G. Melief

# Exercise using pytest in a class

class Employee:
    """A class modelling a employee's first and last name and annual salary"""


    def __init__(self, first_name, last_name, salary):
        """Initialize employee's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """Give the employee a raise"""
        self.salary += salary_raise