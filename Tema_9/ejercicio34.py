# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal

cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
x = 1
sueldos_entre_100_y_300 = 0
sueldos_mayor_a_300 = 0

while x <= cantidad_empleados:
    sueldo = int(input("Ingrese su sueldo: "))
    if 100 <= sueldo <= 300:
        sueldos_entre_100_y_300 += 1
    elif sueldo > 300:
        sueldos_mayor_a_300 += 1
    else:
        continue
    x += 1

print(f"Cantidad de empleados con sueldos entre $100 y $300: {sueldos_entre_100_y_300}")
print(f"Cantidad de empleados con sueldos mayores a 300: {sueldos_mayor_a_300}")