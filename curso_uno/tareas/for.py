lista = []
mayor = 0
suma = 0

def validar_e_ingresar_numero()-> int:
    numero = input("Ingrese un numero : ")
    while not numero.isdigit():
        numero = input("ERROR re-ingrese un numero : ")

    return numero


def sumar(valor_uno: int, valor_dos: int)-> int:
    return valor_uno + valor_dos


def promedio_lista(suma: int, lista: list)-> float:
    return suma / len(lista)


def mostrar_lista(lista: list):
    for num in lista:
        print(num,end = " ")


def encontrar_repetidos(lista: list):
    conteo = {}
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1

    for clave, valor in conteo.items():
        if valor > 1:
            print(f"Se repitio el {clave} en {valor} ocasiones")


def mayor_lista(mayor: int,numero: int,item: int):
    if not item:
        mayor =  numero
    else:
        if mayor < numero:
            mayor = numero

    return mayor


for elemento in range(5):
    numero_ingresado = int(validar_e_ingresar_numero())    
    lista.append(numero_ingresado)
    suma = sumar(suma,numero_ingresado)
    mayor = mayor_lista(mayor,numero_ingresado,elemento)


mostrar_lista(lista)
print(f"\nLa suma de todos es: {suma}\nEl promedio de todo es : {promedio_lista(suma, lista)}\nEl mayor es: {mayor}")
encontrar_repetidos(lista)
     