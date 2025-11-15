# Exercise 7-6 From 'Python Crash Course'
# 15-11-2025 G. Melief

# Exercise using input, while loop, conditional test and three ways to stop the loop

age_prompt = "\nTell me your age to determine the ticket price: "
age_prompt += "\nEnter a negative value to quit. "
price_message = "The ticket price is €"
age = 0 # To determine 'age' variable

# Use conditional test in the while loop to stop the loop
print("\nThis is the loop with the conditional test")
while age >= 0:
    age = int(input(age_prompt))
    if age >= 0: # For quitting the loop without print
        if age < 3:
            print(price_message + "0")
        elif age < 13:
            print(price_message + "10")
        else:
            print(price_message + "15")

# Use an active variable to stop the loop
print("\nThis is the loop with the active flag")
active = True
while active:
    age = int(input(age_prompt))
    if age < 0:
        active = False # For quitting the loop without print
    elif age < 3:
        print(price_message + "0")
    elif age < 13:
        print(price_message + "10")
    else:
        print(price_message + "15")

# Use break statement to exit if the user enters 'quit'
print("\nThis is the loop with the break statement")
break_prompt = "\nTell me your age to determine the ticket price: "
break_prompt += "\nEnter 'quit' when you are finished. "
while True:
    age = input(break_prompt)
    if age == "quit":
        break # For quitting the loop with break statement
    else:
        age = int(age) # Change the age string to int type
    if age < 3:
        print(price_message + "0")
    elif age < 13:
        print(price_message + "10")
    else:
        print(price_message + "15")