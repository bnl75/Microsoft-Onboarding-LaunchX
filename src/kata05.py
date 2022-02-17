####### Ejercicio 1 #######
# Crear variables para almacenar las dos distancias:
tierra = 149597870
jupiter = 778547200

# Calcular la distancia entre planetas en kilómetros:
distanciaKilometros = jupiter - tierra
print("{} km".format(distanciaKilometros))

distanciaMillas = distanciaKilometros * 0.621
print("{} mi".format(distanciaMillas))



####### Ejercicio 2 #######
# Almacenar las entradas del usuario:
tierra = input('Ingresa la distancia del sol a la Tierra: ')
jupiter = input('Ingresa la distancia del sol a Júpiter: ')

# Convierte las cadenas de ambos planetas a números enteros:
tierra = int(tierra)
jupiter = int(jupiter)

# Realizar el cálculo y determinar el valor absoluto:
distanciaKilometros = jupiter - tierra
print("{} km".format(abs(distanciaKilometros)))

# Convertir de KM a Millas:
distanciaMillas = distanciaKilometros * 0.621
print("{} mi".format(abs(distanciaMillas)))