# Exercise 8-9 From 'Python Crash Course'
# 27-11-2025 G. Melief

# Exercise using lists in a function

# Function that calls a list and print each message
def show_messages(messages):
    '''Function that uses a loop to print all messages in a list'''
    for message in messages:
        print(message)

# The list
messages = ['hello', 'welcome', 'goodbye', 'see you later']
# The function call
show_messages(messages)