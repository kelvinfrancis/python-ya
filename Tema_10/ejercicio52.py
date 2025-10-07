# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

cantidad = int(input("Ingrese la cantidad de puntos: "))
primero = 0
segundo = 0
tercero = 0
cuarto = 0


for x in range(cantidad):
    print(f"Coordenada {x + 1}")
    eje_x = int(input("Ingrese el eje x: "))
    eje_y = int(input("Ingrese el eje y: "))
    print("\n")

    if eje_x > 0 and eje_y > 0:
        primero += 1
    elif eje_x < 0 and eje_y > 0:
        segundo += 1
    elif eje_x < 0 and eje_y < 0:
        tercero += 1
    elif eje_x > 0 and eje_y < 0:
        cuarto += 1

print(f"Cantidad de puntos del primer cuadrante: {primero}")
print(f"Cantidad de puntos del segundo cuadrante: {segundo}")
print(f"Cantidad de puntos del tercer cuadrante: {tercero}")
print(f"Cantidad de puntos del cuarto cuadrante: {cuarto}")

