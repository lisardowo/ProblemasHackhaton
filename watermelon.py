"""Watermelon: Dado el peso entero de una sandía, el programa debe 
determinar si se puede dividir en dos partes de peso 
par y positivo. Si es posible, debe imprimir "SI"; de lo contrario, "NO"."""

peso = int(input("Ingrese el peso de la sandía: "))
if peso % 2 == 0 and peso > 2:
    print("SI")
else:
    print("NO")
