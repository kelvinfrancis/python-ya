# Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).

# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

x = int(input("Ingrese el valor de X (diferente de cero): "))
y = int(input("Ingrese el valor de Y (diferente de cero): "))

if x > 0 and y > 0:
    print(f"({x},{y}) se encuentra en el cuadrante 1.")
elif x < 0 and y > 0:
    print(f"({x},{y}) se encuentra en el cuadrante 2.")
elif x < 0 and y < 0:
    print(f"({x},{y}) se encuentra en el cuadrante 3.")
elif x > 0 and y < 0:
    print(f"({x},{y}) se encuentra en el cuadrante 4.")
else:
    print("No ingreso valores validos")