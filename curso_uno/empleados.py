from data_empleados import *
from random import randint, choice


def cargar_lista_empleados_random(lista: list, cantidad: int)->None:
    # Utilizamos el 20000 para ir incrementando de a 1 los legajos y asegurarnos que no sean repetidos.
    EDAD_MIN = 18
    EDAD_MAX = 65
    next_legajo = 20000
    for _ in range(cantidad):
        legajo = next_legajo
        next_legajo += 1
        genero = choice (["f", "m"])
        nombre = choice(nombres_m) if genero == "m" else choice(nombres_f)
        apellido = choice(apellidos)
        edad = randint(EDAD_MIN, EDAD_MAX)
        calle = f"calle {randint(10, 99)} nro {randint(100, 999)}"
        localidad = choice(localidades)
        provincia = choice(provincias)
        # Email va a pasar el nombre + el apellido a minusculas y elige un dominio random de data_empleados
        email = f"{nombre.lower()+apellido.lower() + choice(dominios)}"
        sector = choice(sectores)
        sueldo = float(randint(20000, 50000))

        lista.append(new_empleado(legajo, nombre, apellido, genero, edad, calle, localidad, provincia, email, sector, sueldo))


def new_empleado(legajo, nombre, apellido, genero, edad, calle, localidad, provincia, email, sector, sueldo):
    empleados = {}
    empleados["legajo"] = legajo
    empleados["nombre"] = nombre
    empleados["apellido"] = apellido
    empleados["edad"] = edad
    empleados["genero"] = genero
    empleados["calle"] = calle
    empleados["localidad"] = localidad
    empleados["provincia"] = provincia
    empleados["email"] = email
    empleados["sector"] = sector
    empleados["sueldo"] = sueldo
    return empleados


def mostrar_empleados(empleados:list):
    print("                         ****Lista de Empleados****")
    print(" Legajo Nombre Apellido Genero Edad Calle Localidad Provincia Email Sector Sueldo")
    print("---------------------------------------------------------------------------------")

    for empleado in empleados:
        mostrar_empleado(empleado)
        print()

    print("---------------------------------------------------------------------------------")


def mostrar_empleado(un_empleado):
    print(f" {un_empleado["legajo"]} {un_empleado["nombre"]:>15}  {un_empleado["apellido"]:>15}  {un_empleado["edad"]:>2}  {un_empleado["genero"]} {un_empleado["calle"]:>15}  {un_empleado["localidad"]:>15}  {un_empleado["provincia"]:>15}  {un_empleado["email"]:>15}  {un_empleado["sector"]:>15}  {un_empleado["sueldo"]:10.2f} ")


def empleado_segun_legajo(lista,legajo)-> list:
    retornar_lista = []
    for empleado in lista:
        if empleado["legajo"] == legajo:
            retornar_lista.append(empleado)
            break
    return retornar_lista
    
def nombre_sector_empleado(lista):
    retornar_lista = []
    for emp in lista:
        retornar_lista.append((emp["nombre"],emp["sector"]))
    return retornar_lista

def mostrar_lista_tuplas(lista):
    for tupla in lista:
        for el in tupla:
            print(f"{el:15}", end = "")
        print()