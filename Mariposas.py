"""ecibir las coordenadas de tres puntos y determinar si no están alineados en una línea recta. Debe imprimir "SI" si no lo están y "NO" en caso contrario.
"""
"""Debe calcular el área de una corona circular (una rosca) a partir de la longitud X de un corte tangente a su círculo interior"""

# mariposa 1 (x, y)
# mariposa 2 (a, b)
# mariposa 3 (c, d)

# si y , b, d son iguales -> devolver SI, de lo contrario devolver no 



mariposa1 = input('Coordenadas mariposa 1 (x,y): ').split(",")
mariposa2 = input('Coordenadas mariposa 2 (a,b): ').split(",")
mariposa3 = input('Coordenadas mariposa 3 (c,d): ').split(",")



if mariposa1[1] == mariposa2[1] == mariposa3[1]:   
    print("SI")
elif mariposa1[0] == mariposa2[0] == mariposa3[0]:
    print("SI")
else:
    print("NO")

