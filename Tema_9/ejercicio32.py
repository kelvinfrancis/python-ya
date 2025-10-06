# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.


x = 1
mayor_igual_7 = 0
menor_a_7 = 0
while x <= 10:
    nota = int(input("Ingrese la nota del alumno: "))
    if nota < 7:
        menor_a_7 += 1
    else:
        mayor_igual_7 += 1
    x += 1

print(f"La cantidad de estudiantes con notas mayores o iguales a 7 es: {mayor_igual_7}")
print(f"Cantidad de estudiantes con notas menores a 7 es: {menor_a_7}")