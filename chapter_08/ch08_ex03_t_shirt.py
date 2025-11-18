# Exercise 8-2 From 'Python Crash Course'
# 18-11-2025 G. Melief

# Exercise defining a function with parameters

def make_shirt(size, text):
    """Display a message with the size and the text on the shirt"""
    print(f"You ordered a T-Shirt in the size {size.upper()} and the print "
          f"{text.title()}")

# Call the function with positional arguments
make_shirt("xl", "i love python")

# Call the function with keyword arguments
make_shirt(size = "xl", text = "i love python")