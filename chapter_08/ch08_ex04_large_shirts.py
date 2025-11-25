# Exercise 8-4 From 'Python Crash Course'
# 18-11-2025 G. Melief

# Exercise defining a function with default parameters

def make_shirt(size="large", text="i love python"):
    """Display a message with the size and the text on the shirt"""
    print(f"You ordered a T-Shirt in the size {size.capitalize()} and the print "
          f"{text.title()}")

# Call the function with default arguments
make_shirt()

# Call the function with medium size and default text
make_shirt("medium")

# Call the function with not default size and not default text
make_shirt("small", text ="i love coffee")