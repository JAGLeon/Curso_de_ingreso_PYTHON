lista = [{"a":"b"},{"c":"d"},{"e":"f"}]

for dic in lista:
    for x, y in dic.items():
        print(f"{x}   =>   {y}")


def mostrar_lista_tuplas():
    for tupla in lista:
        for el in tupla:
            print(f"{el:15}" , end = "")
        print()

def mapear_lista_nombre_sector(lista):
    lista_retorno = []
    for emp in lista:
        lista_retorno.append((emp["nombre"], emp["sector"]))
    return lista_retorno

def filtrar_empleados_sector(lista,sector):
    lista_filtrada = []
    for emp in lista:
        if emp["sector"] == sector:
            lista_filtrada.append(emp)
    return lista_filtrada

def mapear_campo_lista(lista,campo) -> list:
    lista_retorno = []
    for emp in lista:
        lista_retorno.append(emp[campo])
    return lista_retorno
    
def promedio_campo_sector(lista,sector,campo):
    empleados_sector = filtrar_empleados_sector(lista,sector)
    sueldos = mapear_campo_lista(empleados_sector,campo)
    print(promedio_lista(sueldos))

def promedio_lista(numeros):
    validar_lista(lista)
    if len(numeros) > 0:
        return sumar_lista(numeros) / len(numeros)
    raise Exception("ERROR! Lista vacia")

def validar_lista(lista):
    if not isinstance(lista,list):
        raise TypeError("Se esperaba una lista")
    
def sumar_lista(lista):
    validar_lista(lista)
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma