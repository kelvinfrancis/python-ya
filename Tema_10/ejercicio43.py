# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio. Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado.

sum = 0
for x in range(10):
    num = int(input("Ingrese un valor: "))
    sum += num

promedio = sum / 10
print(f"Suma total de los 10 valores: {sum}")
print(f"Promedio: {promedio}")
    