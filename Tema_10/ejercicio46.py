# Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)

# Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. Lo primero que se hace es cargar una variable que indique la cantidad de valores a ingresar. Dicha variable se carga antes de entrar a la estructura repetitiva for.

n = int(input("Ingrese un valor: "))
mayor_igual_1000 = 0
for x in range(n):
    valor = int(input("Ingrese un numero entero: "))
    if valor >= 1000:
        mayor_igual_1000 += 1

print(f"De {n} valores ingresados, {mayor_igual_1000} eran mayores o iguales a 1000.")