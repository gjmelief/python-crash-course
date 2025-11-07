# Exercise 5-10 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Exercise to check for duplicates in two lists

# Make lists with existing usernames and new usernames
current_users = ['gert-jan', 'ester', 'boris', 'valerie', 'rex']
new_users = ['boris', 'valerie', 'rex', 'lily', 'harry']

# Loop through the list to check for duplicates and output a msg
for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user.capitalize()} is not available, choose another username.')
    else:
        print(f'{new_user.capitalize()} is available.')