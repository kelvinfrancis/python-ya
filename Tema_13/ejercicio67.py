# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

texto = input("Ingrese una oración: ")
vocales = ['a', 'e', 'i', 'o', 'u']
texto_min = texto.lower()
cantidad = 0

for x in texto_min:
    if x in vocales:
        cantidad += 1

print(f"La cantidad de vocales es: {cantidad}")
