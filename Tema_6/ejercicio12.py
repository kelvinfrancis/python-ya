# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

nota1 = int(input("Ingrese la primera calificación: "))
nota2 = int(input("Ingrese la segunda calificación: "))
nota3 = int(input("Ingrese la tercera calificación: "))
suma = nota1 + nota2 + nota3
promedio = suma / 3

if promedio >= 7:
    print("Promocionado")
else:
    print("Reprobado")