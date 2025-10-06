# Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

primera_lista = []
segunda_lista = []
x = 1

while x <= 15:
    valor = int(input("Ingrese un valor a la lista 1: "))
    primera_lista.append(valor)

    valor_2 = int(input("Ingrese un valor a la lista 2: "))
    segunda_lista.append(valor_2)
    x += 1

suma_1 = sum(primera_lista)
suma_2 = sum(segunda_lista)

if suma_1 > suma_2:
    print(f"Lista 1 es mayor, suma total: {suma_1}")
else:
    print(f"Lista 2 es mayor, suma total: {suma_2}")