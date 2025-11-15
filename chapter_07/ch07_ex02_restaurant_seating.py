# Exercise 7-2 From 'Python Crash Course'
# 12-11-2025 G. Melief

# Exercise for the input function. Convert the string to int and compare to int

group_size = input("What is the size of your party? ")
group_size = int(group_size) # Convert string to int
if group_size > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")