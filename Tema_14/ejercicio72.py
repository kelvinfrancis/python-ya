# Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.

lista = [1, 200, 3, 400, 5, 600, 7, 8]
mayor100 = 0
for item in lista:
    if item > 100:
        mayor100 += 1
print(lista)
print(f"La cantidad de enteros mayores a 100 en la lista es: {mayor100}")