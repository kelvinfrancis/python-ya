# Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.

nombres = []
mas_de_5_caracteres = 0
for _ in range(5):
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)

for name in nombres:
    if len(name) >= 5:
        mas_de_5_caracteres += 1

print(f"Cantidad de nombres con 5 o más caracteres: {mas_de_5_caracteres}")