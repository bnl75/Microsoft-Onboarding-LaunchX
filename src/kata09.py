####### Ejercicio 1 #######
# Función para leer 3 tanques de combustible y muestre el promedio
def informe(tanque1, tanque2, tanque3):
    return 'Informe de tanques de combustible:'.title() + "\nTanque 1: {tanque1}\nTanque 2: {tanque2}\nTanque 3: {tanque3}\nPROMEDIO: {promedio}".format(tanque1=tanque1, tanque2=tanque2, tanque3=tanque3, promedio = ((tanque1 + tanque2 + tanque3) / 3))

# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(informe(7, 10, 4))

# Función promedio 
def promedio(listaValores):
    total = sum(listaValores)
    totalElementos = len(listaValores)
    numPromedio = total / totalElementos
    return "El promedio es: {}".format(numPromedio)

print(promedio([7, 10, 4]))

# Actualiza la función
def informe(tanque1, tanque2, tanque3):
    return 'Informe de tanques de combustible:'.title() + "\nTanque 1: {tanque1}\nTanque 2: {tanque2}\nTanque 3: {tanque3}\nPROMEDIO: {promedio}".format(tanque1=tanque1, tanque2=tanque2, tanque3=tanque3, promedio = promedio([tanque1, tanque2, tanque3]))

print(informe(12, 4, 8))



####### Ejercicio 2 #######
# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno
def informePreciso(horaPrelanzamiento, tiempoVuelo, nombreDestino, tanqueExterno, tanqueInterno):
    return '\n\n\nInforme preciso de la misión'.title() + "\n\nDestino: {nombreDestino}\nHora de prelanzamiento: {horaPrelanzamiento} horas\nTiempo de vuelo: {tiempoVuelo} horas\nTanque externo: {tanqueExterno} l\nTanque interno: {tanqueInterno} l".format(nombreDestino=nombreDestino, horaPrelanzamiento=horaPrelanzamiento, tiempoVuelo=tiempoVuelo, tanqueExterno=tanqueExterno, tanqueInterno=tanqueInterno)

print(informePreciso(10, 75, "Viaje a Marte", 389, 978))

# Escribe tu nueva función de reporte considerando lo anterior
def informePreciso(nombreDestino, *minutos, **combustible):
    return f"""\n\n\n
    Destino: {nombreDestino}
    Minutos del viaje: {sum(minutos)} minutos
    Combustible disponible: {sum(combustible.values())} litros
    """

print(informePreciso("Viaje a Marte", 15, 17, 92, principal=784, externo=895))

# Escribe tu nueva función
def informePreciso(nombreDestino, *minutos, **combustible):
    informacionPrecisa = f"""
    Destino: {nombreDestino}
    Minutos del viaje: {sum(minutos)} minutos
    Combustible disponible en tanque izquierdo: {sum(combustible.values())}
    """
    for nombreTanque, litros in combustible.items():
        informacionPrecisa += f"El tanque {nombreTanque} tiene: {litros} litros\n"
    return informacionPrecisa

print(informePreciso("Viaje a Marte", 15, 17, 92, principal=784, externo=895))