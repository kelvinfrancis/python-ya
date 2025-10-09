# Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura.

print("Primera persona: ")
nombre1 = input("Ingrese su nombre: ")
edad1 = int(input("Ingrese la edad: "))
altura1 = float(input("Ingrese la altura: "))

print("\nSegunda persona: ")
nombre2 = input("Ingrese su nombre: ")
edad2 = int(input("Ingrese la edad: "))
altura2 = float(input("Ingrese la altura: "))

if altura1 > altura2:
    print(f"{nombre1} tiene mayor altura.")
else:
    print(f"{nombre2} tiene mayor altura.")
