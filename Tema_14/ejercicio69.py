# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

numeros = []

for _ in range(5):
    num = int(input("Ingrese un numero entero: "))
    numeros.append(num)

print(f"La suma de los numeros es: {sum(numeros)}")