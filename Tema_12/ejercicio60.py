# Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
# Mostrar la suma de los valores ingresados.

decision = "si"
suma = 0

while decision == "si":
    valor = int(input("Ingrese un valor entero: "))
    suma += valor
    decision = input("Desea seguir ingresando valores ? (si/no): ").lower()

print(f"La suma total de los valores es: {suma}")