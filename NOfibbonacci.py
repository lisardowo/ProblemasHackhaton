n = int(input("Ingresa el número de términos: "))
a, b = 0, 1
#a, b = b, a + b
fib = a + b
for NOfib in range(1, n):
        if NOfib < fib:
            print(NOfib, end=' ')
        else:
            a, b = b, fib 
            fib = a + b

