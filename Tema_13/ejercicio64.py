# Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".

mail = input("Ingrese el mail: ")
cantidad = 0

for x in mail:
    if x == "@":
        cantidad += 1

if cantidad == 1:
    print("Contiene una sola @")
else:
    print("Incorrecto")