# Maak een lijst met pizza's
pizzas = ['margherita', 'diavolo', 'quatro formaggio', 'salami']

# # Output de pizzas list met een for loop
# for pizza in pizzas:
#     print(pizza.title())

# Output de pizza list in een zin met een for loop
# for pizza in pizzas:
#     print(f'Ik hou van pizza {pizza}!\n')

# # Output een zin voor na de for loop
# print('Pizza is fantastisch')

# Kopieer pizzas naar friend_pizzas
friend_pizzas = pizzas[:]

# Voeg een pizza toe aan pizza
pizzas.append('bora')

# Voeg een pizza toe aan friend_pizzas
friend_pizzas.append('meat lovers')

# Print de lijsten met for loops
print("Mijn favoriete pizza's zijn:")
for pizza in pizzas:
    print(pizza)

print("\nMijn vriend zijn favoriete pizza's zijn:")
for pizza in friend_pizzas:
    print(pizza)