"""leer tres números reales (x, y, z) y calcular el resultado de una fórmula matemática específica que los involucra.



"""
x = float(input('x'))
y = float(input('y'))
z = float(input('z'))

def f(x, y, z):
    resultado = 0
    resultado = (((2 * x + y)/z) * ((pow(y, 3))- z)) / (((x + (2 * y) + (3 * z)) / (z - (2 * y) - (3 * x))) + (pow(x, 2)) + (pow(z, 2)))
    return resultado

resultado = f(x, y, z)
print(f'El resultado es: {resultado}')