# Realizar un programa que lea los lados de n triángulos, e informar:

# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

n = int(input("Ingrese la cantidad de triangulos: "))
equilatero = 0
isosceles = 0
escaleno = 0
triangulos = []

for x in range(n):
    print(f"Triangulo {x + 1}:")
    lado_1 = int(input("Ingrese el primer lado: "))
    lado_2 = int(input("Ingrese el segundo lado: "))
    lado_3 = int(input("Ingrese el tercer lado: "))
    print("\n")

    if lado_1 == lado_2 and lado_2 == lado_3:
        equilatero += 1
        triangulos.append('equilatero')
    elif lado_1 == lado_2 and lado_2 != lado_3 or lado_2 == lado_3 and lado_3 != lado_1 or lado_1 == lado_3 and lado_3 != lado_2:
        isosceles += 1
        triangulos.append('isósceles')
    else:
        escaleno += 1
        triangulos.append('escaleno')

for item in range(len(triangulos)):
    print(f"El triangulo {item + 1} es: {triangulos[item]}")

print("\n")
print(f"Cantidad de equilateros: {equilatero}")
print(f"Cantidad de isósceles: {isosceles}")
print(f"Cantidad de equilateros: {escaleno}")


