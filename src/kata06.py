####### Ejercicio 1 #######
# Creamos la lista planets y mostramos el número de planetas:
planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno']
print('Número de planetas:', len(planets))

# Agregamos a plutón y mostramos el último elemento:
planets.append('Plutón')
print('Último planeta:', planets[-1])



####### Ejercicio 2 #######
# Lista de planetas:
planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno']

# Solicitamos el nombre de un planeta:
planetaIngresado = input('Ingresa el nombre de un planeta, debe empezar con mayúscula: ')

# Busca el planeta en la lista:
elementoLista = planets.index(planetaIngresado)

# Muestra los planetas más cercanos al sol:
print('Hay {planetasAnteriores} planetas más cercanos al sol antes que {planetaIngresado}, los cuales son:'.format(planetasAnteriores = elementoLista, planetaIngresado = planetaIngresado))
print(planets[0:elementoLista])

# Muestra los planetas más lejanos al sol:
print('Hay {planetasPosteriores} planetas más lejanos al sol después que {planetaIngresado}, los cuales son:'.format(planetasPosteriores = (len(planets) - 1) - elementoLista, planetaIngresado = planetaIngresado))
print(planets[elementoLista + 1:])