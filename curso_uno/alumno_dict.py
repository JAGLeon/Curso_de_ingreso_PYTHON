
def mostrar_alumno(un_alumno:dict)->None:  
    print(f" {un_alumno["legajo"]} {un_alumno["nombre"]:>10}  {un_alumno["nota_p1"]:2}  {un_alumno["nota_p2"]:2}  {un_alumno["genero"]}  {un_alumno["promedio"]:2.2f}")  


alumnos = [  
    {"legajo": 20000, "nombre": "Juan", "genero": "m",  
    "nota_p1": 6, "nota_p2": 7, "promedio": 6.50},  
    {"legajo": 20001, "nombre": "Juana", "genero": "f",
    "nota_p1": 6, "nota_p2": 7, "promedio": 6.58},
    {"legajo": 20002, "nombre": "Maria", "genero": "m",  
    "nota_p1": 6, "nota_p2": 7, "promedio": 6.50},  
    {"legajo": 20003, "nombre": "Luis", "genero": "m",  
    "nota_p1": 6, "nota_p2": 7, "promedio": 6.50},  
    {"legajo": 20004, "nombre": "Sofia", "genero": "m",  
    "nota_p1": 6, "nota_p2": 7, "promedio": 6.50}  
]

for alumno in alumnos:  
    mostrar_alumno(alumno) 