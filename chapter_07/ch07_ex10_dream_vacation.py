# Exercise 7-10 From 'Python Crash Course'
# 17-11-2025 G. Melief

# Exercise using while loop and a dictionary

# Create an empty dictionary
dream_vacation = {}

# Set flag for repeating the poll
polling_active = True

# While loop while repeat = True
while polling_active == True:
    # Ask for the user's name
    name = input("\nHello user, what is your name? ")

    # Poll user about their dream vacation destination
    destination = input(f"Tell me {name.title()}, what is your dream vacation destination? ")

    # Store the user's name and destination in a dictionary
    dream_vacation[name] = destination

    # Ask the user to quit or not and set the repeat flag according
    repeat = input("Would you like another person te respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# Show the result
print("\n------Poll Results-----")
for name, destination in dream_vacation.items():
    print(f"{name.title()} would really like to go {destination.title()}!")
