# Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos.

sueldo = int(input("Ingrese su sueldo: $"))
if sueldo > 3000:
    print("Debes abonar impuestos.")
else:
    print("No debes abonar impuestos.")