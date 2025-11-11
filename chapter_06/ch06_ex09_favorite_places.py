# Exercise 6-9 From 'Python Crash Course'
# 11-11-2025 G. Melief

# Exercise for looping through a dictionary with keys and a list as value

favorite_places = {
    "gert-jan": ["rotterdam", "london", "berlin"],
    "ester": ["paris", "barcelona", "antwerp"],
    "boris": ["efteling", "disney", "den haag"],
}

# Print all the information from the dictionary
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
