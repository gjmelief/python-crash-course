# Exercise 5-9 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Make a list of five usernames including 'admin'. Loop through the list and make a msg.
# Add an if test to check for empty list

usernames = []

# Check if the list is empty
if usernames:
    # For loop for the messages, different msg for the admin
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, welcome back')
else:
    print('The list of usernames is empty. First add an user')