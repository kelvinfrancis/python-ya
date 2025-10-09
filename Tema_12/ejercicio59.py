# Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente o si son iguales.

nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if nombre1 > nombre2:
    print(f"{nombre1} es mayor alfabéticamente.")
elif nombre2 > nombre1:
    print(f"{nombre2} es mayor alfabéticamente.")
else:
    print("Son iguales alfabéticamente.")