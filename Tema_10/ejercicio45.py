# Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.

multiplos_3 = 0
multiplos_5 = 0

for x in range(10):
    valor = int(input("Ingrese el valor: "))
    if valor % 3 == 0:
        multiplos_3 += 1
    if valor % 5 == 0:
        multiplos_5 += 1

print(f"Multiplos de 3: {multiplos_3}")
print(f"Multiplos de 5: {multiplos_5}")