# Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y año.

# Ejemplo: dia:10 mes:2 año:2018

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if mes <= 3:
    print(f"La fecha {dia}/{mes}/{anio} al primer trimestre")
elif mes <= 6:
    print(f"La fecha {dia}/{mes}/{anio} al segundo trimestre")
elif mes <= 9:
    print(f"La fecha {dia}/{mes}/{anio} al tercer trimestre")
elif mes <= 12:
    print(f"La fecha {dia}/{mes}/{anio} al cuarto trimestre")
else:
    print("Ingrese una fecha valida.")