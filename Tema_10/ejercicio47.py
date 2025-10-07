# Ha llegado nuevamente la parte fundamental, que es el momento donde uno desarrolla individualmente un algoritmo para la resolución de un problema.

# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

n = int(input("Ingrese la cantidad de pares de datos: "))
triangulos = []
superficie_mayor_12 = 0

for _ in range(n):
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    superficie = base * altura
    triangulo = [base, altura, superficie]
    triangulos.append(triangulo)

for x in range(len(triangulos)):
    print(f"Triangulo {x + 1}: base = {triangulos[x][0]}, altura = {triangulos[x][1]}, superficie = {triangulos[x][2]}")
    if triangulos[x][2] > 12:
        superficie_mayor_12 += 1

print(f"La cantidad de triangulos con superficie mayor a 12 es: {superficie_mayor_12}")