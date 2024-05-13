from random import randint

def contar_entero_lista(lista,target):
    validar_lista(lista)
    contador = 0
    for i in range(len(lista)):
        if lista[i] == target:
            contador += 1
    return contador

def buscar_entero(lista,target):
    validar_lista(lista)
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

def entero_en_lista(lista,target):
    validar_lista(lista)
    return buscar_entero(lista,target) != -1

def menor_lista(lista):
    validar_lista(lista)
    if len(lista) > 0:
        for i in range(len(lista)):
            if lista[i] == lista[0] or lista[i] < menor: #ingresa por corto circuito
                menor = lista[i]

        return menor
    
    raise ValueError("ERROR! Lista vacia")

def maximo_lista(lista):
    validar_lista(lista)
    if len(lista) > 0:
        flag = True
        for i in range(len(lista)):
            if flag or lista[i] > mayor: #ingresa por corto circuito
                flag = False
                mayor = lista[i]

        return mayor
    
    raise ValueError("ERROR! Lista vacia")

def promedio_lista(numeros):
    validar_lista(lista)
    if len(numeros) > 0:
        return sumar_lista(numeros) / len(numeros)
    raise Exception("ERROR! Lista vacia")

def sumar_lista(lista):
    validar_lista(lista)
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def mostrar_lista(lista):
    validar_lista(lista)
    for i in range(len(lista)):
        print(lista[i], end= " ")
    print()

def cargar_enteros_random(cant,desde,hasta,lista):
    validar_lista(lista)
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde,hasta))

def cargar_lista_random(cant,desde,hasta):
    numeros = []
    cargar_enteros_random(cant,desde,hasta,numeros)
    return numeros

def ordenar_lista_ascendente(lista):
    validar_lista(lista)
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i+1,tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def ordenar_lista_descendente(lista):
    validar_lista(lista)
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i+1,tam):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def sorteador(lista:list)->None:
    validar_lista(lista)
    from time import sleep
    sleep(5)
    print(f"EL QUE GANO ES {lista[randint(0,len(lista)-1)]}")


def ordenar_lista(lista,orden = True):
    validar_lista(lista)
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i+1,tam):
            if (orden and lista[i] > lista[j]) or (not orden and lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def validar_lista(lista):
    if not isinstance(lista,list):
        raise TypeError("Se esperaba una lista")