from fuc_paralelas import *
TAM = 10
legajos = []
nombres = []
generos = []
notas_p1 = []
notas_p2 = []
promedios = []

cargar_alumnos(legajos,nombres,generos,notas_p1,notas_p2,promedios,TAM)
mostrar_alumnos(legajos,nombres,generos,notas_p1,notas_p2,promedios)
orden_por_promedios(legajos,nombres,generos,notas_p1,notas_p2,promedios)
mostrar_alumnos(legajos,nombres,generos,notas_p1,notas_p2,promedios)