# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.

suma = 0
x = 1
while x <= 10:
    valor = int(input("Indique un numero: "))
    suma += valor
    x += 1

promedio = suma / 10
print(f"Suma de los 10 valores es: {suma}\nPromedio: {promedio}")