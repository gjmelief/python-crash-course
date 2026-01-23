# Exercise 10-6 From 'Python Crash Course'
# 22-01-2026 G. Melief

# Exercise using a try-except block

print("Give me two numbers, and I will add them together.")
print("Press 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can not input text")
    else:
        print(answer)