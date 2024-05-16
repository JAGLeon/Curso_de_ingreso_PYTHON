from data_warehouse import * 

def buscar_entero(lista,target):
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

def entero_en_lista(lista,target):
    return buscar_entero(lista,target) != -1

def calcular_promedio(a,b):
    return (a+b)/2

def mostrar_alumnos(legs,names,genders,notesP1,notesP2,proms):
    print("                   ****Lista de Alumnos****")
    print(f"Legajo   | Nombre    | Genero | NotaP1 | NotaP2 |   Promedio|")
    print("--------------------------------------------------------------")

    for i in range(len(legs)):
        mostrar_alumno(legs[i],names[i],genders[i],notesP1[i],notesP2[i],proms[i])
    print()

def mostrar_alumno(legajo,nombre,genero,notaP1,notaP2,promedio):
    print(f"{legajo}     {nombre:>10}     {genero}       {notaP1:2}        {notaP2:2}      {promedio:5.2f}")

def cargar_lista_datos(lista_destino,lista_origen,cant):
    for i in range(cant):
        lista_destino.append(lista_origen[i])

def cargar_enteros_random(lista,cant,desde,hasta):
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde,hasta))

def cargar_lista_notas(lista,cant):
    NOTA_MIN = 1
    NOTA_MAX = 10
    cargar_enteros_random(lista,cant,NOTA_MIN,NOTA_MAX)


def cargar_legajos(lista,cant):
    from random import randint
    LEGAJO_MIN = 20000
    LEGAJO_MAX = 30000
    for _ in range(cant):
        legajo = randint(LEGAJO_MIN,LEGAJO_MAX)
        while entero_en_lista(lista,legajo):
            legajo = randint(LEGAJO_MIN,LEGAJO_MAX)
        lista.append(legajo)


def calcular_promedios(lista_1,lista_2,lista_3):
    for i in range(len(lista_1)):
        lista_3.append(calcular_promedio(lista_1[i],lista_2[i]))


def cargar_alumnos(legs,names,genders,notesP1,notesP2,proms,cant):
    cargar_legajos(legs,cant)
    cargar_lista_datos(names,nombres,cant)
    cargar_lista_datos(genders,generos,cant)
    cargar_lista_notas(notesP1,cant)
    cargar_lista_notas(notesP2,cant)
    calcular_promedios(notesP1,notesP2,proms)

def orden_por_promedios(legajos,nombres,generos,notas_p1,notas_p2,promedios,ascendente = False):
    tam = len(legajos)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if (ascendente and promedios[i] > promedios[j]) or (not ascendente and promedios[i] < promedios[j]):
                swaps_valores(legajos,i,j)
                swaps_valores(nombres,i,j)
                swaps_valores(generos,i,j)
                swaps_valores(notas_p1,i,j)
                swaps_valores(notas_p2,i,j)
                swaps_valores(promedios,i,j)

def swaps_valores(lista,i,j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux 