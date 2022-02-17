def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()


def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()


def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("No se encontró el archivo: config.txt")



def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encontró el archivo: config.txt")
    except IsADirectoryError:
        print("config.txt no se puede leer porque es una carpeta")



def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encontró el archivo: config.txt")
    except IsADirectoryError:
        print("config.txt no se puede leer porque es una carpeta")
    except (BlockingIOError, TimeoutError):
        print("No se puede leer el archivo porque hay mucha carga en el sistema")



def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"


def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"



def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"