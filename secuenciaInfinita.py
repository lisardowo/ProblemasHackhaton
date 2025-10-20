n = int(input("Ingresa n: "))
v = 1
contador = 0
SoR = 1

while contador < n:
    print(v, end=' ')
    contador += 1
    if v == 5:
        SoR = -1
    elif v == 1:
        SoR = 1
    v += SoR