# Exercise 10-5 From 'Python Crash Course'
# 21-01-2026 G. Melief

# Exercise adding text to a file

from pathlib import Path

path = Path('chapter_10/guest_book.txt')
guests = []
while True:
    print("---Welcome Guest!---")
    new_guest = input("Please state your full name: \n"
                  "Enter 'quit' to stop\n")
    if new_guest == "quit":
        break
    guests.append(new_guest)

guest_str = "\n".join(guests)
path.write_text(guest_str)