# Exercise 8-13 From 'Python Crash Course'
# 27-11-2025 G. Melief

# Exercise using a dictionary in a function

def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Build the user profile
user_profile = build_profile('gert-jan', 'melief',
                             location='spijkenisse',
                             occupation='process operator',
                             study='python')

print(user_profile)