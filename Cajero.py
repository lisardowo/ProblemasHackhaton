"""saldo empieza en $1000. tres opciones. Para hacer un
retiro,  'R', seguido del monto a retirar. Para hacer un
depósito, 'D', seguido del monto a depositar. 
consultar  saldo,  'C', en este caso, el cajero debe
imprimir en pantalla el saldo disponible, con el prefijo '$'. Finalmente, para salir y
terminar de usar el cajero, el usuario ingresa el carácter 'S"""


saldo = 1000
operacion = input("Ingrese la operación R, D, C, S:  ").upper()
while operacion != 'S':
    match operacion:
        case 'R':
            monto = int(input("Ingrese el monto a retirar: "))
            saldo -= monto
            operacion = input("Ingrese la operación R, D, C, S:  ").upper()
        case 'D':
            monto = int(input("Ingrese el monto a depositar: "))
            saldo += monto
            operacion = input("Ingrese la operación R, D, C, S:  ").upper()
        case 'C':
            print(f'Saldo disponible: ${saldo}')
            operacion = input("Ingrese la operación R, D, C, S:  ").upper()
        case 'S':
            print('Saliendo...')