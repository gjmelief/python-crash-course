from pathlib import Path

path = Path("chapter_10/pi_digits.txt")
# contents = path.read_text().rstrip()
# print(contents)

contents = path.read_text()
for line in contents.splitlines():
    print(line)