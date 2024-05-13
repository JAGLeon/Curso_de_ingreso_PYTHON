def duplicar_lista(valores): 
    for i in range(len(valores)):
        valores[i] = valores[i] * 2





# --------------------------
lista = [3, 5, 6, 8, 3]
print(lista) # [3, 5, 6, 8, 3]

# aca usamos la funcion duplicar lista
duplicar_lista(lista)

print(lista) # [6, 10, 12, 16, 6]
