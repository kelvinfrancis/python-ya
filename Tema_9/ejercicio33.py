# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

n = int(input("Ingrese la cantidad de personas: "))
x = 1
suma_alturas = 0
while x <= n:
    altura = float(input("Ingrese la altura de la persona en metros: "))
    suma_alturas += altura
    x += 1

promedio_alturas = suma_alturas / n
print(f"El promedio de altura de las {n} personas es: {round(promedio_alturas, 2)}")