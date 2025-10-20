
import math

"""Fer escapando
Fernando estaba viajando en el tiempo cuando termino siendo perseguido por un
robot en el futuro.¡Oh no! Pero Fer programó su máquina del tiempo para
teletransportarlo después de T segundos. El robot avanzara Ci metros del
segundo i al i+1, mientras que Fer avanza V.
Ayuda a Fer a escapar, es decir que en cualquier momento Q, tal que 0 &lt;= Q &lt;= T,
Además Q pertenece a los enteros, Fer siempre debe estar adelante del robot por
lo menos un metro.
NOTA: V es constante en todo momento
Entrada
Tres enteros T, R, F siendo el tiempo que durará la persecución, la posición de
inicial del robot, la posición inicial de Fer.
En la siguiente línea T representando Ci.
Salida
Un entero no negativo siendo la mínima V para que Fer escape.

"""
T, R , F = map(int, input("Ingresa en el siguiente orden: Tiempo, posicion del robot, posicion de Fer: : ").split())
distanciaAcumulada = 0
Vmaxima = 0
Vnecesaria = 0

Ci_lista = list(map(int, input(f"Ingresa las {T} distancias del robot separadas por espacios: ").split()))

for i in range(T):
    Ci = Ci_lista[i]
    distanciaAcumulada += Ci
    Vnecesaria = (R - F + distanciaAcumulada + 1) / (i + 1)
    if Vnecesaria > Vmaxima:
        Vmaxima = Vnecesaria

print(math.ceil(Vmaxima))




