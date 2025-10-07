# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

suma = 0

print("\nTurno de la mañana:")
for x in range(5):
    edad = int(input("Ingrese la edad del alumno: "))
    suma += edad

promedio_manana = round(suma / 5, 2)
suma = 0

print("\nTurno de la tarde:")
for x in range(6):
    edad = int(input("Ingrese la edad del alumno: "))
    suma += edad

promedio_tarde = round(suma / 6, 2)
suma = 0

print("\nTurno de la noche:")
for x in range(11):
    edad = int(input("Ingrese la edad del alumno: "))
    suma += edad

promedio_noche = round(suma / 11, 2)

print(f"\nPromedio de la tanda de la mañana: {promedio_manana}")
print(f"Promedio de la tanda de la tarde: {promedio_tarde}")
print(f"Promedio de la tanda de la noche: {promedio_noche}")

if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print(f"La tanda de la mañana tiene el promedio de edades más alto.")
elif promedio_tarde > promedio_noche and promedio_tarde > promedio_manana:
    print(f"La tanda de la tarde tiene el promedio de edades más alto.")
else:
    print(f"La tanda de la noche tiene el promedio de edades más alto.")