####### Ejercicio 1 #######
# Declara dos variables
new_planet = ''
planets = []

# Escribe el ciclo while solicitado:
while new_planet.lower() != 'done':
    if len(new_planet) > 0:
        planets.append(new_planet)
    new_planet = input('Ingresa un planeta: ')



####### Ejercicio 2 #######
# Escribe tu ciclo for para iterar en una lista de planetas:
for planet in planets:
    print('Planeta', planets.index(planet) + 1, ':', planet)