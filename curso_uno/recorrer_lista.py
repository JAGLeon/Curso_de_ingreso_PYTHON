def promedio_entero(a,b):
    return (a + b) // 2

def busqueda_binaria(lista,target):
    inf = 0
    sup = len(lista) - 1

    while inf <= sup:
        medio = promedio_entero(inf,sup)
        if lista[medio] == target:
            return medio
        elif target > lista[medio]:
            inf = medio + 1
        else:
            sup = medio - 1 
