from empleados import *


empleados = []
TAM = 5

cargar_lista_empleados_random(empleados, TAM)
mostrar_empleados(empleados)


#0 pedir un legajo y mostrar al empleado con ese legajo

# legajo = int(input("Ingrese un legajo"))
# empleado_por_legajo = (empleado_segun_legajo(empleados,legajo))
# if empleado_por_legajo != None:
#     mostrar_empleado(empleado_por_legajo)
# else: 
#     print(f"No existe un empleado con ese legajo : {legajo}")


#1 mostrar por consola los nombres y sectores de los empleados





resp = nombre_sector_empleado(empleados)
mostrar_lista_tuplas(resp)
