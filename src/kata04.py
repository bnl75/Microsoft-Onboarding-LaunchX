####### EJERCICIO 1 #######
# El texto con el que trabajarás es el siguiente:
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Primero, divide el texto en cada oración para trabajar con su contenido:
oraciones = text.split('. ')

# Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho:
palabrasClave = ["average", "temperature", "distance"]

# Crea un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
for oracion in oraciones:
    for palabraClave in palabrasClave:
        if palabraClave in oracion:
            print(oracion)

# Finalmente, actualiza el bucle(ciclo) para cambiar C a Celsius:
for oracion in oraciones:
    for palabraClave in palabrasClave:
        if palabraClave in oracion:
            print(oracion.replace('C', 'Celsius'))



####### EJERCICIO 2 #######
# Datos con los que vas a trabajar:
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

# Primero, crea un título para el texto. Debido a que este texto trata sobre la gravedad en la Tierra y la Luna, úsalo para crear un título significativo. Utiliza las variables en lugar de escribir:
title = "La gravedad de la {}".format(planet)
print(title)

# Ahora crea una plantilla de cadena multilínea para contener el resto de la información. En lugar de usar kilómetros, debes convertir la distancia a metros multiplicando por 1,000.
informacion = f""" 
Planeta {planet}.
La gravedad en la {name} es de: {gravity * 1000} m/s2 
"""

# Finalmente, usa ambas variables para unir el título y los hechos.
plantilla = """{0} 
{1} 
""".format(title.title(), informacion)
print(plantilla)

# Ahora usa información de una luna diferente para ver si la plantilla todavía funciona:
name = 'Marte '
gravity  = 0.00143
planet = 'Ganímedes'

# Comprueba la plantilla:
print(plantilla)

# Nueva plantilla:
print(plantilla.format(name, gravity, planet))