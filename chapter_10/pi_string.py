from pathlib import Path

path = Path('chapter_10/pi_million_digits.txt')
# contents = path.read_text().rstrip()
# print(contents)

contents = path.read_text()
# for line in lines:
#     print(line)

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))