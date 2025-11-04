# Exercise 5-1 From 'Python Crash Course'
# 18-10-2025 G. Melief

# Conditional Test 1
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

# Conditional Test 2
animal = "bird"
print("\nIs animal == 'bird'? I predict True.")
print(animal == "bird")

print("\nIs animal == 'dog'? I predict False.")
print(animal == "dog")

# Conditional Test 3
vehicle = "airplane"
print("\nIs vehicle == 'airplane'? I predict True.")
print(animal == "vehicle")

print("\nIs vehicle == 'car'? I predict False.")
print(vehicle == "car")

# Conditional Test 4
food = "pizza"
print("\nIs food == 'pizza'? I predict True.")
print(food == "pizza")

print("\nIs food == 'pancakes'? I predict False.")
print(food == "pancakes")

# Conditional Test 5
country = "france"
print("\nIs country == 'france'? I predict True.")
print(country == "france")

print("\nIs country == 'spain'? I predict False.")
print(country == "spain")

# Conditional Test 6
print("\nTest 6")
city = "rotterdam"
print("Is city == 'rotterdam'? I predict True.")
print(city == "rotterdam")

print("\nIs city == 'spijkenisse'? I predict False")
print(city == "spijkenisse")

# Conditional Test 7. Test using !=
print("\nTest 7")
beer = "la chouffe"
print("Is beer != 'heineken'? I predict True.")
print(beer != "heineken")

print("\nIs beer != 'la chouffe'? I predict False.")
print(beer != "la chouffe")

# Conditional Test 8. Test using .lower()
print("\nTest 8")
car = "Audi"
print("Is car == 'Audi'? I predict True.")
print(car == "Audi")

print("\nIs car.lower() == 'audi'? I predict True")
print(car.lower() == "audi")

# Conditional Test 9. Numerical tests
print("\nTest9")
num = 13
print("Is num == 13? I predict True.")
print(num == 13)

print("\nIs num != 13? I predict False.")
print(num != 13)

print("\nIs 14 > num? I predict True")
print(14 > num)

print("\nIs 15 < num? I predict False.")
print(15 < num)

print("\nIs 13 >= num? I predict True")
print(13 >= num)

print("\nIs 76 <= num? I predict False")
print(76 <= num)

# Conditional Test 10. Tests using 'and' and 'or'
print("\nTest 10")
age_0 = 18
age_1 = 37

print("\nIs 20 > 18 and is 20 < 37? I predict True.")
print(20 > age_0 and 20 < age_1)

print("\nIs 20 > 18 or is 40 < 37? I predict True")
print(20 > age_0 or 40 < age_1)

# Conditional Test 11. Test whether an item is in a list
foods = ["pizza", "fries", "pancakes", "pasta"]
print("\nTest 11")
print("\nIs 'pizza' in foods? I predict True")
print("pizza" in foods)

print("\nIs 'broccoli' in foods? I predict False")
print("broccoli" in foods)

# Conditional Test 12. Test whether an item is not in a list
print("\nTest 12")
print("\nIs 'broccoli' not in foods? I predict True")
print("broccoli" not in foods)

print("\nIs 'fries not in foods? I predict False")
print("fries" not in foods)