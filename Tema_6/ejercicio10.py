# Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 == num2:
    print("Son iguales.")
elif num1 > num2:
    print(f"El {num1} es mayor que {num2}")
else:
    print(f"El {num2} es mayor que {num1}")