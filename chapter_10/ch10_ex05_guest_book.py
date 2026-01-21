# Exercise 10-5 From 'Python Crash Course'
# 21-01-2026 G. Melief

# Exercise adding text to a file

from pathlib import Path

path = Path('chapter_10/guest_book.txt')
while True:
    print("---Welcome Guest!---")
    guest = input("Please state your full name: \n"
                  "Enter 'quit' to stop\n")
    if guest == "quit":
        break
    else:
        path.write_text(guest)