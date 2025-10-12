# Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.

nombre = input("Ingrese su nombre: ").lower()
primera_letra = nombre[0]
vocales = ['a', 'e', 'i', 'o', 'u']

if primera_letra in vocales:
    print("El nombre comienza con vocales.")
else:
    print("El nombre no comienza con vocales.")