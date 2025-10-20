from math import pi

"formula A=π( x/2)^2"

x = float(input('Longitud del corte: '))


def area(x):
    area = pi * ((x/2)**2)
    return area

respuesta = area(x)
print(f'El área es: {respuesta}')