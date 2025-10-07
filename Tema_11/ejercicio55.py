# Mostrar la tabla de multiplicar del 5 empleando primero el while y seguidamente de nuevo empleando el for.

"""Tabla del 5 con while"""
x = 1
print("Tabla del 5 con while:")
while x < 13:
    print(f"{x} x {5} = {x * 5}")
    x += 1

"""Tabla del 5 con for"""
print("\nTabla del 5 con for:")
for x in range(5, 51, 5):
    print(x)