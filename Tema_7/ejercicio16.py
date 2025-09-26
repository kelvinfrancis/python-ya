# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

num = int(input("Ingrese el número: "))

if num > 0:
    print(f"El número {num} es positivo")
elif num < 0:
    print(f"El número {num} es negativo")
else:
    print(f"El número {num} es nulo")