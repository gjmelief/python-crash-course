# Exercise 8-14 From 'Python Crash Course'
# 27-11-2025 G. Melief

# Exercise using a dictionary in a function

def make_car(manufacturer, model, **car_info):
    '''Build a dictionary with information about a car'''
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_profile = make_car('tesla', 'model 3', color='white', type="awd")

print(car_profile)