# Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercero número: "))

if num1 > num2 and num1 > num3:
    print(f"El {num1} es el mayor")
elif num2 > num3:
    print(f"El {num2} es el mayor")
else:
    print(f"El {num3} es el mayor")