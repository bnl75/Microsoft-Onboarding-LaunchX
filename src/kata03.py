# EJERCICIO 01:
####### Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
####### Escribe una expresión de prueba para calcular si necesita una advertencia.
####### Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

velocidadAsteriode = 49 #km/s
if (velocidadAsteriode > 25):
    print('¡CUIDADO! El asteroide viene muy rápido')
else:
    print('No hay de qué preocuparse')





# EJERCICIO 02:
####### Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
####### Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
####### Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

velocidadAsteriode = 19 #km/s

if (velocidadAsteriode == 20):
    print('¡Mira arriba! Se ve un asteroide')
elif (velocidadAsteriode >= 20):
    print('Probablemente se vea un asteroide en el cielo')
else:
    print('Esta vez no se verá un asteroide')





# EJERCICIO 03:
####### Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
####### Para probar el código, prueba con varias velocidades y tamaños
####### Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

dimensionAsteroide = 30 #metros
velocidadAsteriode = 19 #km/s

if (dimensionAsteroide < 25):
    print('Esta vez no se verá un asteroide')
elif (dimensionAsteroide > 25 and dimensionAsteroide < 1000):
    if (velocidadAsteriode == 20):
        print('¡Mira arriba! Se ve un asteroide')
    elif (velocidadAsteriode > 20):
        print('Probablemente se vea un asteroide en el cielo')
    else:
        print('Si tienes suerte, verás un asteroide')
else:
    print('Es el asteroide más grande nunca antes visto')