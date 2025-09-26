# Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El primer número es mayor. \nSuma: {num1 + num2} \nDiferencia: {num1 - num2}")
else:
    print(f"El segundo número es mayor. \nProducto: {num2 * num1} \nDivisión: {num2 / num1}")