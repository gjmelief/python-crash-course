# Exercise 8-14 From 'Python Crash Course'
# 27-11-2025 G. Melief

# Exercise using a dictionary in a function

def make_car(manufacturer, model, **car_options):
    '''Build a dictionary with information about a car'''
    car_info = {'Manufacturer': manufacturer.title(),
                'Model': model.title(),
    }
    # Use a loop for adding the options
    for option, value in car_options.items():
        car_info[option.title()] = value.title()

    return car_info

car_profile = make_car('tesla', 'model 3', color='white', type="awd")

print(car_profile)