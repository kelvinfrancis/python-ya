# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

suma = 0

for x in range(10):
    valor = int(input("Ingrese un numero: "))
    # el indice es de 0 a 9, cuando es 4 ya completa 5 vueltas
    if x > 4:
        suma += valor

print(f"La suma de los ultimos 5 valores es: {suma}")
