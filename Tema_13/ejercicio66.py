# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
# " ", en cambio una cadena vacía es ""

texto = input("Ingrese una oración: ")
espacios = 0
for x in texto:
    if x == " ":
        espacios += 1

print(f"Cantidad de espacios: {espacios}")