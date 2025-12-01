# Exercise 8-15 From 'Python Crash Course'
# 01-12-2025 G. Melief

# Exercise using import

def print_models(*designs):  # '*' So that there can be multiple arguments
    '''Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    '''
    completed_models = []
    for design in designs:
        print(f"Printing model: {design}")
        completed_models.append(design)
    return completed_models  # completed_models wil be returned for use outside function


def show_completed_models(completed_models):
    '''Display all completed models.'''
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)