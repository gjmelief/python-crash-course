# opdracht 4-8
# Maak een list van de cubes van 1 t/m 10 (cube = tot de macht 3). Output de list met een for loop

# Maak de cubes lijst
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

# Output de cubes list met een for loop
for cube in cubes:
    print(cube)

# Nogmaals de opdracht maar dan met een comphrension
cubes_comp = [value ** 3 for value in range(1, 11)]
for cube in cubes_comp:
    print(cube)
print(cubes_comp)