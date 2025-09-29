# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if mes == 12:
    if dia == 25:
        print(f"La fecha {dia}/{mes}/{anio} es navidad.")
    else:
        print("No es navidad.")
else:
    print("No es navidad.")