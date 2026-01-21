# Exercise 10-3 From 'Python Crash Course'
# 21-01-2026 G. Melief

# Exercise making code simpler

from pathlib import Path

path = Path('chapter_10/pi_digits.txt')
# contents = path.read_text().rstrip()
# print(contents)

contents = path.read_text()
for line in contents.splitlines():
    print(line)