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
        print(f"{self.first_name.title()} salary is €{self.salary}.")
        self.salary += salary_raise
        print(f"{self.first_name.title()} get's a raise of €{salary_raise}!"
              f"\n{self.first_name.title()} has now a salary of {self.salary}!")

worker_0 = Employee('gert-jan', 'melief', 50000)
worker_0.give_raise()