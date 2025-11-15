# Exercise 7-5 From 'Python Crash Course'
# 15-11-2025 G. Melief

# Exercise using input, while loop and conditional test

price_message = "The ticket price is €"
free = str(0)
ten = str(10)
fifteen = str(15)
while True:
    age = int(input("Tell me your age to determine the ticket price: "))
    if age < 3:
        print(price_message + free)
    elif age < 13:
        print(price_message + ten)
    else:
        print(price_message + fifteen)