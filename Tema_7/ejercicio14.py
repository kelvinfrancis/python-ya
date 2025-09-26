# Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
# Si el promedio es >=7 mostrar "Promocionado".
# Si el promedio es >=4 y <7 mostrar "Regular".
# Si el promedio es <4 mostrar "Reprobado".

nota_1 = int(input("Ingrese la primera nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercera nota: "))

suma = nota_1 + nota_2 + nota_3
promedio = suma / 3

if promedio >= 7:
    print("Promocionado")
elif 4 >= promedio < 7:
    print("Regular")
else:
    print("Reprobado")