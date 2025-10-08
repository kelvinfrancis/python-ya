# Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.

# el mensaje se repetira 10 veces y sumara el valor con la variable suma
suma = 0
for _ in range(10):
    valor = int(input("Ingrese su valor:"))
    suma += valor

print(f"La suma total es: {suma}")
