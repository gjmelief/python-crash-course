# Exercise 7-8 From 'Python Crash Course'
# 17-11-2025 G. Melief

# Exercise using while loop and a list

# list with sandwiches
sandwich_orders =["carpaccio", "tuna", "pastrami", "salmon"]
finished_sandwiches = [] # Empty list for storing the finished sandwiches

# Loop through the list and move the latest item to current_sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    # Print the current_sandwich
    print(f"\nI made you a {current_sandwich} sandwich.")
    # append current_sandwich to finished_sandwiches
    finished_sandwiches.append(current_sandwich)

# Print the finished_sandwiches list
for sandwich in finished_sandwiches:
    print(f"\nYou finished a {sandwich} sandwich.")