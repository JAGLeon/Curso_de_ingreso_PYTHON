from tareas.pack.funciones_listas import *
TAM = 3

legajos = [15000,16000,17000]
nombres = ["leon","seba","lucho"]
generos = ["m","m","m"]
notas_p1 = [8,8,6]
notas_p2 = [4,7,5]
promedios = [6,7.5,5.5]
# legajos = []
# nombres = []
# generos = []
# notas_p1 = []
# notas_p2 = []
# promedios = []

def error_str(txt):
    if not isinstance(txt, str):
        raise TypeError("Se esperaba un caracter")

def validar_numeros_listas(max, min, texto):
    if not isinstance(max, int) or not isinstance(min, int):
        raise TypeError("Se esperaba un entero")

    error_str(texto)

    num = int(input(f"Ingrese {texto}: "))

    while num < max or num > min:
        num = int(input(f"RE-Ingrese {texto}: "))
    return num

def validar_nombre(nombre):
    error_str(nombre)

    while len(nombre) < 3:
        nombre = input("RE-Ingrese un nombre: ")
    return nombre

def validar_genero(tipo):
    error_str(tipo)

    while tipo != "m" and tipo != "f":
        tipo = input("RE-Ingrese género: ")
    return tipo

def promedios_notas(primer_nota, segunda_nota):
    promedio = (primer_nota + segunda_nota) / 2
    return promedio

def mostrar_datos_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios):
    for i in range(TAM):
        print(f"{legajos[i]:20} | {nombres[i]:20} | {generos[i]:20} | {notas_p1[i]:20} | {notas_p2[i]:20} | {promedios[i]:20}"\
            , end = "\n")

def orden_por_promedios(ascendente = True):
    for i in range(TAM - 1):
        for j in range(i + 1, TAM):
            if (ascendente and promedios[i] > promedios[j]) or (not ascendente and promedios[i] < promedios[j]):
                swaps_variables(legajos,i,j)
                swaps_variables(nombres,i,j)
                swaps_variables(generos,i,j)
                swaps_variables(notas_p1,i,j)
                swaps_variables(notas_p2,i,j)
                swaps_variables(promedios,i,j)

def swaps_variables(lista,i,j):
    validar_lista(lista)
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

# for _ in range(TAM):
#     num_legajo = validar_numeros_listas(10000, 20000, "legajo")
#     legajos.append(num_legajo)

#     nombre_ingresado = input("Ingrese su nombre: ")
#     nombres.append(validar_nombre(nombre_ingresado))

#     genero_ingresado = input("Ingrese género: ")
#     generos.append(validar_genero(genero_ingresado))

#     nota_uno = validar_numeros_listas(1, 10, "nota primer parcial")
#     notas_p1.append(nota_uno)

#     nota_dos = validar_numeros_listas(1, 10, "nota segundo parcial")
#     notas_p2.append(nota_dos)

#     promedios.append(promedios_notas(nota_uno, nota_dos))

orden_por_promedios()
mostrar_datos_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)

