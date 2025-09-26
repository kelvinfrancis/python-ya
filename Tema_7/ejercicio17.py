# Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.

num = int(input("Ingrese el número entero: "))

if  0 <= num <= 9:
    print(f"El número {num} es de una cifra.")
elif 10 <= num <= 99:
    print(f"El número {num} es de dos cifras.")
elif num <= 999:
    print(f"El número {num} es de tres cifras.")
else:
    print(f"ERROR: número {num} contiene más de tres cifras.")