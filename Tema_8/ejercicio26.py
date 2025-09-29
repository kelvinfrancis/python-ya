# De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:

# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.

# b) Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.

# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

sueldo = int(input("Ingrese su sueldo: "))
antiguedad = int(input("Ingrese sus años de antigüedad: "))

if sueldo < 500 and antiguedad >= 10:
    print(f"Le toca un 20% de aumento, en total sería: {(sueldo * 0.20) + sueldo}")
elif sueldo < 500 and antiguedad < 10:
    print(f"Le toca un 5% de aumento, en total sería: {(sueldo * 0.05) + sueldo}")
elif sueldo >= 500:
    print(f"No te toca aumento, tu sueldo permanece igual: {sueldo}")