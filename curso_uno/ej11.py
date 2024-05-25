from pack.funciones_listas import *

CANT = 5
MIN = 1
MAX = 10

# numeros = []
# cargar_enteros_random(CANT,MIN,MAX,numeros)
# mostrar_lista(numeros)

numeros = cargar_lista_random(CANT,MIN,MAX)
mostrar_lista(numeros)



sumatoria = sumar_lista(numeros)
print(sumatoria)



try:
    print(promedio_lista(numeros))
except Exception as ex:
    print(ex)




try:
    print(maximo_lista(numeros))
except ValueError as ex:
    print(ex)




try:
    print(menor_lista(numeros))
except ValueError as ex:
    print(ex)


# def entero_en_lista(lista,target):
#     for i in range(len(lista)):
#         if lista[i] == target:
#             return True
#     return False

numero = 20

# if entero_en_lista(numeros,numero):
#     print(f"El numero {numero}, esta en la lista")
# else:
#     print(f"El numero {numero}, no esta en la lista")



def buscar_entero(lista,target):
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1

indice_result = buscar_entero(numeros,numero)
if indice_result != -1:
    print(f"{numero} esta en la lista, indice {indice_result}")
else:
    print(f"{numero} no esta en la lista")



if entero_en_lista(numeros,numero):
    print(f"El numero {numero}, esta en la lista")
else:
    print(f"El numero {numero}, no esta en la lista")

x = 10

cantidad = contar_entero_lista(numeros,x)
print(cantidad)