# Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.

# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num = int(input("Ingrese un número positivo:"))

if num <= 0:
    print(f"El número {num} no es positivo")
elif 1 <= num < 10:
    print(f"El número {num} es de un digito")
elif 10 <= num <= 99:
    print(f"El número {num} es de dos digitos")
else:
    print(f"El número {num} tiene más de dos digitos.")
