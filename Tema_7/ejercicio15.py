# Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercero número: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"El mayor es: {num_1}")
elif num_2 > num_1 and num_2 > num_3:
    print(f"El mayor es: {num_2}")
elif num_3 > num_1 and num_3 > num_2:
    print(f"El mayor es: {num_3}")
else:
    print(f"Todos son iguales.")