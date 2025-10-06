# Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

cantidad = int(input("Ingrese la cantidad de numeros enteros: "))
pares = 0
impares = 0
x = 1

while x <= cantidad:
    valor = int(input("Ingrese un valor: "))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Cantidad de valores: {cantidad}")
print(f"Valores pares: {pares}")
print(f"Valores impares: {impares}")