####### Ejercicio 1 #######
# Crea un diccionario llamado planet con los datos propuestos:
planet = {
    'name': 'Mars',
    'moons': 2
}

# Muestra el nombre del planeta y el número de lunas que tiene:
print("Nombre del planeta: {0}\nNúmero de lunas: {1}".format(planet["name"], planet["moons"]))

# Agrega la clave circunferencia con los datos proporcionados previamente:
planet['circunferencia'] = {
    'polar': 6752,
    'equatorial': 6792
}

# Imprime el nombre del planeta con su circunferencia polar:
print("{0} tiene una circunferencia polar de: {1} km".format(planet["name"], planet["circunferencia"]["polar"]))



####### Ejercicio 2 #######
# Planets and moons:
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de lunas:
lunas = planet_moons.values()

# Agrega el código para contar el número de planetas:
totalPlanetas = len(planet_moons.keys())

# Ciclo para obtener el total de  lunas en todos los planetas
totalLunas = 0
for luna in lunas:
    totalLunas += luna

# División para obtener el promedio
promedio = totalLunas / totalPlanetas

# Mostramos el promedio
print("El promedio de lunas que tiene un planeta es de:", promedio, "lunas")