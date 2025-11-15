# Exercise 7-3 From 'Python Crash Course'
# 12-11-2025 G. Melief

# Exercise for the input function. Ask for number and report if the number is a
# multiple of ten

number = input("Enter a number, and I'll tell you if it is a multiple of ten: ")
number = int(number) # Convert string to int
if number % 10 == 0: # Check if remainder == 0
    print(f"{number} is a multiple of ten!")
else:
    print(f"{number} is not a multiple of ten!")