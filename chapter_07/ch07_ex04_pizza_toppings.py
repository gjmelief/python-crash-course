# Exercise 7-4 From 'Python Crash Course'
# 15-11-2025 G. Melief

# Exercise with input, while loop and a 'quit' value

prompt = "\nTell me what kind of toppings you like on your pizza:"
prompt += "\nEnter 'quit' when  you are finished. "


topping = "" # To define 'topping'
while topping != "quit":
    topping = input(prompt)
    if topping != "quit": # To avoid printing 'quit'
        print(f"I will add {topping} on your pizza.")