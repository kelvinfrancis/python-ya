# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 == num2 and num2 == num3:
    suma = num1 + num2
    print(f"Suma: {num1} + {num2} = {suma}\nMultiplicación: {suma} * {num3} = {suma * num3}")
else:
    print("No son iguales.")