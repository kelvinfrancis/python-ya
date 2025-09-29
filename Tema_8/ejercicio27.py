# Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)

lista = []
for num in range(3):
    num = int(input("Ingrese un número: "))
    lista.append(num)

min = lista[0]
max = lista[0]

for item in lista:
    if item > max:
        max = item
    elif item < min:
        min = item

print(f"La diferencia del mayor {max}, y el menor {min}, es: {max - min}")
