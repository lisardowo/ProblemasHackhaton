"""Domingo de Pascua: A partir de un año A como entrada, el programa debe aplicar un algoritmo 
específico (de Gauss) para calcular y mostrar el día y el mes en que cae el Domingo de Pascua."""

A = int(input("Ingrese un año: "))

B = A // 100 + 1
C = (3 * B) // 4 - 12
E = (A % 19) + 1
F = (8 * B + 5) // 25 - (5 + C)
G = (5 * A) // 4 - (C + 10)
H = (11 * E + 20 + F) % 30
if H == 25:
    if E > 11:
        H += 1
if H == 24:
    H += 1

I = 44 - H
if I < 21:
    I += 30
J = I + 7 - ((G + I) % 7)
if J <= 31:
    D = J
    M = 3
else:
    D = J - 31
    M = 4

print(f"{D} {M}")