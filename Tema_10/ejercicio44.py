# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

mayor_igual_7 = 0
menor_7 = 0

for x in range(10):
    nota = int(input("Ingrese la nota del alumno: "))
    if nota >= 7:
        mayor_igual_7 += 1
    else:
        menor_7 += 1

print(f"Alumnos con notas mayores o iguales a 7: {mayor_igual_7}")
print(f"Alumnos con notas menores a 7: {menor_7}")