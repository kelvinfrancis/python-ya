# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

valores_negativos = 0
valores_positivos = 0
multiplos_15 = 0
suma_pares = 0

for _ in range(10):
    valor = int(input("Ingrese un valor: "))
    if valor < 0:
        valores_negativos += 1
    elif valor > 0:
        valores_positivos += 1
    
    if valor % 15 == 0:
        multiplos_15 += 1
    
    if valor % 2 == 0:
        suma_pares += valor

print("\n")
print(f"Valores negativos: {valores_negativos}")
print(f"Valores positivos: {valores_positivos}")
print(f"Valores multiplos de 15: {multiplos_15}")
print(f"Suma total de valores pares: {suma_pares}")