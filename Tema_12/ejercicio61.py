# Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética.

nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if nombre1 == nombre2:
    print("Son iguales.")
    print(f"Orden alfabético: \n{nombre2}\n{nombre1}")
elif nombre1 > nombre2:
    print(f"Orden alfabético: \n{nombre2}\n{nombre1}")
else:
    print(f"Orden alfabético: \n{nombre1}\n{nombre2}")
