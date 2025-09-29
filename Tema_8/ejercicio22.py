# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda "Todos los números son menores a diez".

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 < 10 and num2 < 10 and num3 < 10:
    print("Todos los números son menores a 10")
else:
    print("NO todos los números son menores a 10")