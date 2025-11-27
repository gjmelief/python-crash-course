# Exercise 8-11 From 'Python Crash Course'
# 27-11-2025 G. Melief

# Exercise using lists in a function with a copy of the original list

def show_messages(messages):
    '''Show the messages'''
    print(f'All the messages:')
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    '''Second function that uses a loop to print all messages in a list.
    After the print the message should move to a new list
    '''
    print('\nSend the messages')
    while messages:
        current_message = messages.pop()
        print(f'The current message is {current_message}')
        sent_messages.append(current_message)

# The list
messages = ['hello', 'welcome', 'goodbye', 'see you later']
sent_messages= []
# The function calls
print('This is the messages list before the function:')
show_messages(messages)
send_messages(messages[:], sent_messages)
print('\nThis is the messages list after the function:')
show_messages(messages)
print('\nThis is the sent_messages list after the function:')
show_messages(sent_messages)