# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 < 10 or num2 < 10 or num3 < 10:
    print("Alguno de los números es menor a diez")
else:
    print("Todos los números son igual o mayor a 10")