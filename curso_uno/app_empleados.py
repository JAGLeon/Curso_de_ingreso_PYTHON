from empleados import *


empleados = []
TAM = 5

cargar_lista_empleados_random(empleados, TAM)
#mostrar_empleados(empleados)


#0 pedir un legajo y mostrar al empleado con ese legajo

legajo = int(input("Ingrese un legajo"))
empleado_por_legajo = (empleado_segun_legajo(empleados,legajo))
mostrar_empleados(empleado_por_legajo)

#1 mostrar por consola los nombres y sectores de los empleados

# resp = nombre_sector_empleado(empleados)
# mostrar_lista_tuplas(resp)

#2 pedir un sector y mostrar los empleados de ese sector

# def empleado_por_columna_valor(lista,columna,valor):
#     retornar_lista = []
#     for emp in lista:
#         if emp[columna] == valor:
#             retornar_lista.append(emp)
#     return retornar_lista

# mostrar_empleados(empleado_por_columna_valor(empleados,"sector","RRHH"))