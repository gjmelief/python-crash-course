# Exercise 10-3 From 'Python Crash Course'
# 21-01-2026 G. Melief

# Exercise writing to a file

from pathlib import Path

print("---Welcome!---")
guest = input("Please state your full name: \n")

path = Path('chapter_10/guest.txt')
path.write_text(guest)