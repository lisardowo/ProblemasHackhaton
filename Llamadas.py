"""
Llamadas telefónicas
El costo de las llamadas telefónicas internacionales depende de la zona
geográfica en la que se encuentre el país destino y del número de minutos
hablados. En la siguiente tabla se presenta el costo del minuto por zona. A cada
zona se le ha asociado una clave.
Construya un programa que le permita calcular e imprimir el costo total de una
llamada.

Entrada

En una línea dos enteros, la clave y el número de minutos de la llamada,
separados por un espacio.

Salida

El costo de la llamada

CLAVE ZONA COSTO POR MINUTO
12  América del Norte $2
15 America Central 2.2
18 America del Sur 4.5
19 Europa 3.5
23 Asia 6
25 África 6
29 Oceanía 5

"""
costos = { 12: 2, 15: 2.2, 18: 4.5, 19: 3.5, 23: 6, 25: 6, 29: 5}
clave, minutos = ((input("clave y minutos: ")).split(","))

clave = int(clave)
minutos = int(minutos)
costoLLamada = costos.get(clave, 0) * minutos
print(costoLLamada)