# Exercise 5-8 From 'Python Crash Course'
# 04-11-2025 G. Melief

# Make a list of five usernames including 'admin'. Loop through the list and make a msg.

usernames = ['admin', 'Gert-Jan', 'Ester', 'Boris', 'Valerie']

# For loop for the messages, different msg for the admin
for username in usernames:
    if username == 'admin':
        print(f'Hello {username}, would you like to see a status report?')
    else:
        print(f'Hello {username}, welcome back')