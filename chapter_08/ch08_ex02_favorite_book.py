# Exercise 8-2 From 'Python Crash Course'
# 18-11-2025 G. Melief

# Exercise defining a function with a parameter

def favorite_book(title):
    """Display a message with the title passed as an argument"""
    print(f"One of my favorite books is {title.title()}.")

# Call the favorite_book functions and pass a book title as argument
favorite_book("way of kings")